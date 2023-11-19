from mesa.component.textlabel import MesaTextLabel
from mesa.flag.core_flag import MesaCoreFlag
import pygame as pg


class MesaButtonText(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.signal = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.callback_result = None

    def get_result(self):
        return self.callback_result

    def set_signal(self, func):
        self.signal = func

    def handle_events(self):
        for event in self.scene.manager.get_events():
            if event.type == pg.MOUSEBUTTONDOWN and self._is_container_hovered():
                if self.signal != MesaCoreFlag.NOT_DECLARED_ON_INIT:
                    self.callback_result = self.signal()
                else:
                    print(f"[DEBUG] No callback has been asigned to {self}")

    def inherit_update(self):
        self.handle_events()

        return super().inherit_update()
