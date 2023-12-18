import pygame as pg
from mesa.container.container import _MesaContainer
from mesa.flag.render_flag import MesaRenderFlag
from mesa.flag.core_flag import MesaCoreFlag


class MesaStackVertical(_MesaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def update_scroll(self):
        self.rel = self.core.mouse_rel

        if self._is_container_hovered():
            if pg.mouse.get_pressed(3)[0]:
                items_total_height = sum(
                    [element.get_real_height() for element in self.elements]
                )
                element_height_coverage = items_total_height - self.height
                # False scrolling fix
                if items_total_height >= self.height:
                    for element in self.elements:
                        element.scrolloffset.y += self.rel[1] * 2
                        if element.scrolloffset.y > 0:
                            element.scrolloffset.y = 0
                        if element.scrolloffset.y < -1 * element_height_coverage:
                            element.scrolloffset.y = -1 * element_height_coverage
                        element.update_rects()

        return super().update_scroll()

    def _compute_elements_positions(self):
        accum = pg.Vector2(0, 0)

        for element in self.elements:
            if element.center_x == MesaRenderFlag.CENTERX:
                if self.surface_type == MesaCoreFlag.CORESURFACE:
                    element.position.x = (
                        pg.display.get_surface().get_width()
                        - element.surface.get_width()
                    ) / 2
                else:
                    element.position.x = (
                        self.surface.get_width() - element.surface.get_width()
                    ) / 2
                element.absolute_position.x = (
                    self.absolute_position.x + element.position.x
                )
            else:
                element.position.x = accum.x + element.marginx
                element.absolute_position.x = (
                    self.absolute_position.x + accum.x + element.marginx
                )
            element.position.y = accum.y + element.marginy

            element.absolute_position.y = (
                self.absolute_position.y + accum.y + element.marginy
            )
            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
            accum.y += element.height + element.marginy * 2
        return super()._compute_elements_positions()
