from mesa import *
import pygame as pg
import time


class RenteckLogo(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(510)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(50)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


class EntryScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = RenteckLogo(self.container, "Renteck")
        self.container.set_as_core()
        self.container.build()

        self.time = time.time()

    def update(self):
        if time.time() - self.time > 1:
            self.manager.go_to("login")
        return super().update()
