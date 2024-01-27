from mesa.core import MesaCore
import pygame as pg
from mesa.scene.scene_manager import MesaSceneManager
from pygame import _sdl2 as SDL2


class MesaScene:
    def __init__(self, core, scene_name, manager) -> None:
        from mesa.container import _MesaContainer

        self.core: MesaCore = core
        # self.renderer = self.core.renderer
        self.name = scene_name
        self.previous_scene = None
        self.can_go_back = False
        self.position = pg.Vector2([0, 0])
        self.manager: MesaSceneManager = manager
        self.manager.add_scene(self)
        self.container: _MesaContainer = None
        self.modals = []
        self.informer = self.core.info_tag
        self.surface = self.core.display
        self.is_active = False
        self.background_color = "white"

    def get_events(self):
        return self.manager.get_events()

    def set_background_color(self, color):
        self.background_color = color

    def resize(self):
        self.surface = self.core.display
        self.container.set_size_as_display()
        self.container.set_position_as_core()
        self.container.build()
        self.container._on_resize()

    def update(self):
        ...

    def update_container(self):
        self.container.__coreupdate__()

    def __coreupdate__(self):
        self.update()
        self.update_container()

    def blit_into_core(self):
        self.core.display.blit(self.surface, self.position)

    def fill_color(self):
        # self.renderer.draw_color = self.background_color
        # self.renderer.draw_rect(self.renderer.get_viewport())
        self.surface.fill(self.background_color)

    def render_container(self):
        self.container.__corerender__()

    def render_modals(self):
        ...

    def render(self):
        ...

    def __corerender__(self):
        self.fill_color()
        self.render_container()
        self.render_modals()
        self.render()
        self.blit_into_core()
