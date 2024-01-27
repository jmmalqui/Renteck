import os
from const import PATH
from mesa.container.container import _MesaContainer
from mesa.flag.core_flag import MesaCoreFlag
from mesa.flag.render_flag import MesaRenderFlag
from mesa.text_buffer.text_buffer import TextBuffer
import pygame as pg


class MesaTextBoxInput(_MesaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.font_name = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.font = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.font_size = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.font_type = "SYS"
        self.text = ""
        self.text_surface = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.bold = False
        self.italic = False
        self.text_background_color = None
        self.antialias = True
        self.text_color = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.buffer = TextBuffer()
        self.text_center_v_flag = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.text_center_h_flag = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.metrics = []
        self.pointer_position = self._get_pointer_position()
        self.active = False
        self.blink = False
        self.tick = 0
        self.offset = pg.Vector2(10, 0)
        self.is_password = False

    def password(self):
        self.is_password = True

    def declare_font_type(self, _type: str):
        # This is subject to change, strings are considered bad practice.
        if _type == "SYS":
            self.font_type = "SYS"
        if _type == "NOSYS":
            self.font_type = "NOSYS"

    def load_ttf(self, ttf):
        self.font_name = ttf

    def center_text_vertical(self):
        self.text_center_v_flag = MesaRenderFlag.TEXT_CENTERED_V

    def center_text_horizontal(self):
        self.text_center_h_flag = MesaRenderFlag.TEXT_CENTERED_H

    def center_text(self):
        self.center_text_horizontal()
        self.center_text_vertical()

    def get_written_text(self):
        return self.buffer.buffer

    def _get_pointer_position(self):
        return (sum([x[4] for x in self.metrics[: self.buffer.pointer]]),)

    def _handle_events(self):
        for event in self.scene.manager.get_events():
            if event.type == pg.TEXTINPUT and self.active:
                self.buffer.add(event.text)
                self.text = self.buffer.buffer
                self._make_text_surface()
                self.buffer.shift_right()
                self.metrics = pg.font.Font.metrics(self.font, self.text)
                self.pointer_position = self._get_pointer_position()

            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_TAB:
                    self.buffer.delete()
                    self.text = self.buffer.buffer
                    self._make_text_surface()
                    self.metrics = pg.font.Font.metrics(self.font, self.text)
                if event.key == 8:
                    self.buffer.pop()
                    self.text = self.buffer.buffer
                    self._make_text_surface()
                    self.metrics = pg.font.Font.metrics(self.font, self.text)
                if event.key == pg.K_LEFT:
                    self.buffer.shift_left()
                if event.key == pg.K_RIGHT:
                    self.buffer.shift_right()
                if event.key == pg.K_RETURN:
                    self.text += "\n"
                    self._make_text_surface()
                    self.metrics = pg.font.Font.metrics(self.font, self.text)
                    self.active = False
                    pg.key.stop_text_input()
                self.pointer_position = self._get_pointer_position()

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.active:
                    self.active = False
                if self._is_container_hovered():
                    if self.active == False:
                        pg.key.start_text_input()
                    else:
                        pg.key.stop_text_input()
                    self.active = not self.active

    def set_text_color(self, text_color):
        if self.text_color == MesaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text_color = text_color
        if self.text_surface != MesaCoreFlag.NOT_DECLARED_ON_INIT:
            if text_color != self.text_color:
                self.text_color = text_color
                self._make_text_surface()

    def set_text_background_color(self, color):
        self.text_background_color = color

    def unset_antialiasing(self):
        self.antialias = False

    def set_bold(self):
        self.bold = True

    def set_italic(self):
        self.italic = True

    def set_font_name(self, font_name):
        self.font_name = font_name

    def set_font_size(self, font_size):
        if self.font_size == MesaCoreFlag.NOT_DECLARED_ON_INIT:
            self.font_size = font_size
        if self.font_size != MesaCoreFlag.NOT_DECLARED_ON_INIT:
            if font_size != self.font_size:
                self.font_size = font_size
                if self.font_type == "SYS":
                    self.font = pg.font.SysFont(
                        self.font_name, self.font_size, self.bold, self.italic
                    )
                elif self.font_type == "NOSYS":
                    self.font = pg.font.Font(
                        os.path.join(PATH, self.font_name), self.font_size
                    )
                self._make_text_surface()

    def set_text(self, text):
        if self.text == MesaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text = text
        if self.text_surface != MesaCoreFlag.NOT_DECLARED_ON_INIT:
            if text != self.text:
                self.text = text
                self._make_text_surface()

    def _make_text_surface(self):
        if self.is_password:
            self.text = "*" * len(self.text)
        self.text_surface = self.font.render(
            self.text,
            self.antialias,
            self.text_color,
            self.text_background_color,
        )

    def late_init(self):
        if self.font_type == "SYS":
            self.font = pg.font.SysFont(
                self.font_name, self.font_size, self.bold, self.italic
            )
        elif self.font_type == "NOSYS":
            self.font = pg.font.Font(os.path.join(PATH, self.font_name), self.font_size)
        self._make_text_surface()
        pg.key.set_text_input_rect(self.rect)
        return super().late_init()

    def inherit_update(self):
        self.tick += 1
        self._handle_events()
        return super().inherit_update()

    def _configure_text_position(self):
        self.text_position = pg.Vector2(0, 0)
        if self.text_center_v_flag == MesaRenderFlag.TEXT_CENTERED_V:
            self.text_position.y = (self.height - self.text_surface.get_height()) // 2
        if self.text_center_h_flag == MesaRenderFlag.TEXT_CENTERED_H:
            self.text_position.x = (self.width - self.text_surface.get_width()) // 2

    def _blink_logic(self):
        if self.tick % 25 == 0:
            self.blink = not self.blink

    def _draw_pointer(self):
        overflow = pg.Vector2(
            self.pointer_position[0] - self.surface.get_width() + self.offset.x + 30, 0
        )
        overflow.x = max(0, overflow.x)
        blink_width = 1
        blink_height = self.font_size + 2
        if self.metrics:
            blink_width = self.metrics[self.buffer.pointer - 1][4]

        pg.draw.rect(
            self.surface,
            [0, 0, 0, 100],
            [
                self.pointer_position[0] + self.offset.x - overflow.x,
                self.text_position.y,
                2,
                blink_height,
            ],
            0,
        )

    def _draw_text(self):
        overflow = pg.Vector2(
            self.pointer_position[0] - self.surface.get_width() + self.offset.x + 30, 0
        )
        if overflow.x > 0:
            self.surface.blit(
                self.text_surface, self.text_position + self.offset - overflow
            )
        else:
            self.surface.blit(self.text_surface, self.text_position + self.offset)

    def render(self):
        self._configure_text_position()
        if self.active:
            self._blink_logic()
            self._draw_pointer()
        self._draw_text()
