from const import APPSIZE
from mesa.core import *
from typing import Dict, Union
from mesa.flag import *
import pygame as pg
from mesa.animation import DynamicObject, Animation
from mesa.animation.easing import *


class MesaSceneManager:
    def __init__(self, core) -> None:
        from mesa.scene.scene import MesaScene

        self.core: MesaCore = core
        self.scenes: Dict["str", MesaScene] = {}
        self.current_scene_name = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.current_scene: Union[
            MesaScene, MesaCoreFlag
        ] = MesaCoreFlag.NOT_DECLARED_ON_INIT
        self.events = []
        self.animation = Animation()
        self.timer = 0
        self.fade_time = 200
        self.begin_fade = False
        self.late_init = True
        self.fade_surf = None
        self.fade_level = DynamicObject(self.animation, 0)

    def set_fade_time(self, time):
        self.fade_time = time

    def set_init_scene(self, scene_name):
        self.current_scene_name = scene_name

    def get_events(self):
        return self.events

    def pump_event(self, event):
        if event:
            self.events.append(event)
        else:
            self.events.clear()

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def update_scene_sizes(self):
        for scene in self.scenes.values():
            scene.resize()

    def update_scene_ids(self):
        self.current_scene = self.scenes[self.current_scene_name]

    def return_to_previous_scene(self):
        previous = self.scenes[self.current_scene_name].previous_scene
        if previous != None:
            self.go_to(previous)

    def go_to(self, scene_name, can_go_back=True):
        previous_scene = self.current_scene_name
        self.current_scene_name = scene_name
        if can_go_back:
            self.scenes[self.current_scene_name].previous_scene = previous_scene
        self.begin_fade = True
        self.fade_level.pulse(
            0,
            150,
            0,
            0,
            self.fade_time,
            ease_in_out_back,
            ease_out_back,
        )

    def resize_current_surface(self):
        if self.current_scene != MesaCoreFlag.NOT_DECLARED_ON_INIT:
            self.current_scene.surface = pg.Surface(pg.display.get_window_size())
            self.current_scene.container.set_size_as_display()
            self.current_scene.container.set_position_as_core()
            self.current_scene.container.build()
            self.current_scene.container._on_resize()

    def update(self):
        self.animation.update()
        if self.late_init:
            self.fade_surf = pg.Surface(APPSIZE, pg.SRCALPHA)
            self.fade_surf.fill("white")
            self.fade_surf.set_alpha(self.fade_level.get_value())
            self.late_init = False
        self.fade_surf.set_alpha(self.fade_level.get_value())
        self.update_scene_ids()
        if self.begin_fade:
            self.timer += 1
        if self.timer == self.fade_time:
            self.begin_fade = False
            self.timer = 0
        self.current_scene.__coreupdate__()

    def render(self):
        self.current_scene.__corerender__()
