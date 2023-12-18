import pygame as pg
from mesa.container.container import _MesaContainer
from mesa.flag.render_flag import MesaRenderFlag


class MesaStackHorizontal(_MesaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def update_scroll(self):
        self.rel = self.core.mouse_rel
        if self._is_container_hovered():
            if pg.mouse.get_pressed(3)[0]:
                for element in self.elements:
                    element.scrolloffset.x += self.rel[0]
                    element.update_rects()

        return super().update_scroll()

    def _compute_elements_positions(self):
        accum = pg.Vector2(0, 0)
        for element in self.elements:
            element.position.x = accum.x + element.marginx
            if element.center_y == MesaRenderFlag.CENTERY:
                element.position.y = (
                    self.surface.get_height() - element.surface.get_height()
                ) / 2
                element.absolute_position.y = (
                    self.absolute_position.y + element.position.y
                )
            else:
                element.position.y = accum.y + element.marginy
                element.absolute_position.y = (
                    self.absolute_position.y + accum.y + element.marginy
                )
            element.absolute_position.x = (
                self.absolute_position.x + accum.x + element.marginx
            )

            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )

            accum.x += element.width + element.marginx * 2
        return super()._compute_elements_positions()
