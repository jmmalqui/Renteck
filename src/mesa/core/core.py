import os
import pygame as pg
from mesa.flag.core_flag import *
from pygame import _sdl2 as sdl
from mesa.info_tag.tag import InfoTagHandler
from mesa.event import EventSystem

os.environ["SDL_IME_SHOW_UI"] = "1"
if "ANDROID_ARGUMENT" in os.environ:
    from jnius import autoclass

    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    InputMethodManager = autoclass("android.view.inputmethod.InputMethodManager")


class MesaCore:
    def __init__(self) -> None:
        from mesa.scene.scene_manager import MesaSceneManager

        pg.init()
        self.ratio = 1
        self.winfo = pg.display.Info()
        if "ANDROID_ARGUMENT" in os.environ:
            self.ANDROID = True
        else:
            self.ANDROID = False
        self.eventsys = EventSystem()
        self.perform_late_init = True
        self.display = None
        self.clock = None
        self.clock_type = None
        self.clock_fps = None
        self.rendering_flags = None
        self.bacgkround_color = None
        self.delta_time = None
        self.caption = None
        self.info_tag = InfoTagHandler(self)
        self.scene_manager = MesaSceneManager(self)
        self.on_debug = False
        self.mouse_rel = [0, 0]

    def get_window_token(self):
        context = PythonActivity.mActivity

        view = context.getCurrentFocus()

        if view:
            window_token = view.getWindowToken()
            return window_token
        else:
            return None

    def hide_keyboard(self):
        if self.ANDROID:
            context = PythonActivity.mActivity

            input_manager = context.getSystemService(Context.INPUT_METHOD_SERVICE)

            window_token = self.get_window_token()

            if window_token:
                input_manager.hideSoftInputFromWindow(window_token, 0)

    def set_application_name(self, title):
        self.caption = title
        pg.display.set_caption(self.caption)

    def set_rendering_flags(self, *flags):
        self.rendering_flags = flags

    def set_clock(self, fps):
        self.clock = pg.time.Clock()
        self.clock_type = MesaCoreFlag.NON_TICK_BUSY_CLOCK
        self.clock_fps = fps

    def set_busy_clock(self, fps):
        self.clock = pg.time.Clock()
        self.clock_type = MesaCoreFlag.TICK_BUSY_CLOCK
        self.clock_fps = fps

    def set_display_size(self, height, width):
        if self.rendering_flags == None:
            self.rendering_flags = 0
            if not self.ANDROID:
                self.display = pg.display.set_mode(
                    [height, width], flags=self.rendering_flags
                )

            else:
                self.display = pg.display.set_mode(
                    [height * 1.5, width * 1.5],
                    pg.SCALED | pg.DOUBLEBUF,
                )
                self.ratio = 1.5

        else:
            flag = self.rendering_flags[0]
            for f in self.rendering_flags[0:]:
                flag |= f
            if not self.ANDROID:
                self.display = pg.display.set_mode([height, width], flag)
            else:
                self.display = pg.display.set_mode(
                    [height * 1.5, width * 1.5],
                    pg.SCALED | pg.DOUBLEBUF,
                )
                self.ratio = 1.5

    def late_init(self):
        if self.clock == None:
            self.set_clock(60)
        if self.bacgkround_color == None:
            self.bacgkround_color = "black"

    def check_events(self):
        self.scene_manager.pump_event(None)
        for event in pg.event.get():
            self.scene_manager.pump_event(event)
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F4:
                    exit()
                if event.key == pg.K_F1:
                    self.on_debug = not self.on_debug
            if event.type == pg.VIDEORESIZE:
                self.scene_manager.update_scene_sizes()

    def set_background_color(self, color):
        self.bacgkround_color = color

    def update(self):
        ...

    def __coreupdate__(self):
        self.mouse_rel = pg.mouse.get_rel()
        self.info_tag.update()
        if self.perform_late_init:
            self.late_init()
            self.perform_late_init = not self.perform_late_init

        self.scene_manager.update()

    def render(self):
        ...

    def __corerender__(self):
        self.scene_manager.render()
        self.render()
        self.info_tag.render()
        pg.display.update()

    def update_dt(self):
        if self.clock_type == MesaCoreFlag.NON_TICK_BUSY_CLOCK:
            self.delta_time = self.clock.tick(self.clock_fps)
        elif self.clock_type == MesaCoreFlag.TICK_BUSY_CLOCK:
            self.delta_time = self.clock.tick_busy_loop(self.clock_fps)

    def run(self):
        while True:
            self.update_dt()
            self.check_events()

            self.__coreupdate__()
            self.__corerender__()
