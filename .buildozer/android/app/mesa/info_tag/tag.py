import os
import pygame as pg
from const import APPSIZE, PATH
from mesa.core import *
from mesa.animation import *
from mesa.style import *

import time


class TagProperty:
    def __init__(self, fill, border, ttl) -> None:
        self.fill = fill
        self.border = border
        self.ttl = ttl


class InfoTagLevels:
    NOTIFY = TagProperty([0, 230, 0], "black", 3)
    ALERT = TagProperty([120, 170, 200], "white", 2.5)
    CRITICAL = TagProperty([240, 0, 0], "white", 4)
    SPECIAL = TagProperty([170, 0, 170], [170, 0, 170], 3)


class InfoTagHandler:
    def __init__(self, core) -> None:
        self.core: MesaCore = core
        self.tags: list[InfoTag] = []
        self.tag_font = pg.font.SysFont("Calibri", 20, False)

    def set_font(self, font_name):
        self.tag_font = pg.font.Font(
            os.path.join(PATH, font_name),
            int(15 * self.core.ratio),
        )

    def inform(self, information, level=InfoTagLevels.NOTIFY):
        if information in [tag.information for tag in self.tags]:
            return
        self.tags.append(InfoTag(self, information, level))
        self.update_tag_ids()

    def update_tag_ids(self):
        tag_num = len(self.tags)
        for tag_id, tag in enumerate(self.tags):
            tag.set_id(tag_num - tag_id - 1)

    def update(self):
        for tag in self.tags:
            tag.update()

    def render(self):
        for tag in self.tags:
            tag.render()


class InfoTag:
    def __init__(self, handler, information, level: TagProperty) -> None:
        self.id = 0
        self.information = information
        self.level = level
        self.handler: InfoTagHandler = handler
        self.animation = Animation()
        self.time = time.time()
        self.x = DynamicObject(self.animation, 0.0)
        self.y = DynamicObject(self.animation, (2160 / 3))
        self.alpha = DynamicObject(self.animation, 255)
        self.text = self.handler.tag_font.render(
            self.information,
            True,
            level.border,
            wraplength=int((1080 // 3) * self.handler.core.ratio) - 20,
        )
        self.surface = pg.Surface(
            [int((1080 // 3) * self.handler.core.ratio), self.text.get_height() + 20],
            pg.SRCALPHA,
        )
        self.rect = pg.Rect([0, 0], self.surface.get_size())

        self.vanishing_time = 1

    def set_id(self, id):
        self.id = id
        y_difference = 0
        for tag in self.handler.tags:
            if tag.id < self.id:
                y_difference += tag.surface.get_height()
        self.y.go_to(
            float(-1 * y_difference),
            40,
            MesaAnimationCurves.EASE_OUT_EXPO,
        )

    def update(self):
        self.elapsed = time.time() - self.time
        self.animation.update()
        self.rect = pg.Rect([0, 0], self.surface.get_size())
        if self.elapsed > self.level.ttl:
            self.y.go_to(
                float(self.surface.get_height()),
                40,
                MesaAnimationCurves.EASE_OUT_EXPO,
            )
        if self.elapsed >= self.level.ttl + self.vanishing_time:
            self.handler.tags.remove(self)
            self.time = time.time()

            self.handler.update_tag_ids()

    def render(self):
        self.surface.fill("black")
        pg.draw.rect(self.surface, self.level.fill, self.rect, 0)
        self.surface.blit(
            self.text,
            [
                self.surface.get_width() / 2 - self.text.get_width() / 2,
                self.surface.get_height() / 2 - self.text.get_height() / 2,
            ],
        )
        self.surface.set_alpha(self.alpha.get_value())
        self.handler.core.display.blit(
            self.surface,
            [
                self.x.get_value(),
                self.handler.core.display.get_height()
                - self.surface.get_height()
                + self.y.get_value(),
            ],
        )
