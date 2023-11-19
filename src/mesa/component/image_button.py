from mesa.component.image import MesaImage
from mesa.flag.core_flag import MesaCoreFlag
import pygame as pg


class MesaImageButton(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.signal = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.callback_result = None

    def get_result(self):
        return self.callback_result

    def set_signal(self, func):
        self.signal = func

    def get_image_rect(self):
        if self.image_pos != MesaCoreFlag.NOT_DECLARED_ON_INIT:
            return pg.Rect(
                self.get_absolute_position() + self.image_pos,
                self.image.get_size(),
            )
        else:
            return pg.Rect(self.get_absolute_position(), self.image.get_size())

    def is_button_hovered(self):
        rect = self.get_image_rect()
        return rect.collidepoint(pg.mouse.get_pos())

    def handle_events(self):
        for event in self.scene.manager.get_events():
            if self.image_pos != MesaCoreFlag.NOT_DECLARED_ON_INIT:
                if (
                    event.type == pg.MOUSEBUTTONDOWN
                    and self.is_button_hovered()
                    and self._is_container_hovered()
                ):
                    if self.signal != MesaCoreFlag.NOT_DECLARED_ON_INIT:
                        self.callback_result = self.signal()
                    else:
                        print(f"[DEBUG] No callback has been asigned to {self}")

    def inherit_update(self):
        self.handle_events()

        return super().inherit_update()
