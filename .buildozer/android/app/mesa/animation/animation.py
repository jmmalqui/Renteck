import time
import pygame as pg
from typing import Union


class Animation:
    def __init__(self):
        self.dynamic_objects: list[DynamicObject] = []

    def update(self):
        for dynamic_object in self.dynamic_objects:
            dynamic_object.update()


class AnimationTypes:
    UNIDIRECTIONAL = 1
    PULSE = 2


class DynamicObject:
    def __init__(
        self,
        animation_manager: Animation,
        animation_object: Union[float, pg.Vector2, pg.Vector3],
    ):
        self.linear_interpolation_position = None
        self.animation_manager = animation_manager
        self.animation_object = animation_object
        self.begin_animation_object = None
        self.animation_manager.dynamic_objects.append(self)
        self.begin_timestamp = time.time()
        self.current_timestamp = time.time()
        self.animation_object_difference = None
        self.animation_function = None
        self.animation_duration = 0
        self.target_animation_object = None
        self.animation_fired = False
        self.animation_type = None

        self.forward_time = 0
        self.back_time = 0
        self.forward_animation = None
        self.back_animation = None
        self.pulse_begin_anim_obj = None
        self.pulse_end_anim_obj = None
        self.going_forward = True
        self.middle_timestamp = None

    def get_value(self):
        return self.animation_object

    def begin_pulsating_movement(self):
        if self.target_animation_object is None:
            return
        if self.current_timestamp >= self.forward_time + self.back_time:
            if (
                type(self.pulse_end_anim_obj) == pg.Vector2
                or type(self.pulse_end_anim_obj) == pg.Vector3
            ):
                self.animation_object = self.pulse_end_anim_obj.copy()
            else:
                self.animation_object = self.pulse_end_anim_obj
            self.animation_fired = False
            self.pulse_end_anim_obj = None
            self.pulse_begin_anim_obj = None
            self.forward_animation = None
            self.back_animation = None
            self.forward_animation = 0
            self.back_animation = 0
            self.animation_type = None

        if (
            self.current_timestamp >= self.forward_time
            and self.going_forward
            and self.animation_fired
        ):
            if (
                type(self.target_animation_object) == pg.Vector2
                or type(self.target_animation_object) == pg.Vector3
            ):
                self.animation_object = self.target_animation_object.copy()

            else:
                self.animation_object = self.target_animation_object
            self.animation_object_difference = (
                self.pulse_end_anim_obj - self.animation_object
            )
            self.middle_timestamp = time.time()
            self.going_forward = False

        if self.going_forward:
            if self.animation_fired:
                if self.forward_time:
                    self.linear_interpolation_position = self.forward_animation(
                        self.current_timestamp / self.forward_time
                    )
                    self.animation_object = (
                        self.pulse_begin_anim_obj
                        + self.linear_interpolation_position
                        * self.animation_object_difference
                    )
        if self.going_forward == False:
            elapsed_time_back = (time.time() - self.middle_timestamp) * 100
            if self.animation_fired:
                if self.back_time:
                    self.linear_interpolation_position = self.back_animation(
                        elapsed_time_back / self.back_time
                    )
                    self.animation_object = (
                        self.target_animation_object
                        + self.linear_interpolation_position
                        * self.animation_object_difference
                    )

    def begin_unidirectional_movement(self):
        if self.target_animation_object is None:
            return
        if self.current_timestamp >= self.animation_duration:
            if (
                type(self.target_animation_object) == pg.Vector2
                or type(self.target_animation_object) == pg.Vector3
            ):
                self.animation_object = self.target_animation_object.copy()
            else:
                self.animation_object = self.target_animation_object
            self.animation_fired = False

        if self.animation_function:
            if self.animation_fired:
                self.linear_interpolation_position = self.animation_function(
                    self.current_timestamp / self.animation_duration
                )
                self.animation_object = (
                    self.begin_animation_object
                    + self.linear_interpolation_position
                    * self.animation_object_difference
                )
        else:
            raise ValueError(
                f"No Animation Function was given.,{self.__class__.__name__}"
            )

    def is_moving(self):
        return self.animation_fired

    def pulse(
        self,
        begin: Union[float, pg.Vector2, pg.Vector3],
        target: Union[float, pg.Vector2, pg.Vector3],
        end: Union[float, pg.Vector2, pg.Vector3],
        forward_t,
        back_t,
        forward_anim_func,
        back_anim_func,
    ):
        self.animation_fired = True
        self.animation_type = AnimationTypes.PULSE
        self.begin_timestamp = time.time()
        self.going_forward = True
        if isinstance(begin, pg.Vector2) or isinstance(begin, pg.Vector3):
            self.animation_object = begin.copy()
            self.pulse_begin_anim_obj = begin.copy()
            self.target_animation_object = target.copy()
            self.pulse_end_anim_obj = end
        else:
            self.animation_object = begin
            self.pulse_begin_anim_obj = begin
            self.target_animation_object = target
            self.pulse_end_anim_obj = end
        self.forward_time = forward_t
        self.back_time = back_t
        self.forward_animation = forward_anim_func
        self.back_animation = back_anim_func
        self.animation_object_difference = target - begin

    def go_to(
        self,
        target: Union[float, pg.Vector2, pg.Vector3],
        duration: float,
        animation_function,
    ):
        self.animation_fired = True
        self.animation_type = AnimationTypes.UNIDIRECTIONAL
        self.begin_timestamp = time.time()
        if type(target) != type(self.animation_object):
            raise TypeError("Data types mismatch")
        if isinstance(self.animation_object, Union[pg.Vector2, pg.Vector3]):
            self.begin_animation_object = self.animation_object.copy()
            self.target_animation_object = target.copy()
        else:
            self.begin_animation_object = self.animation_object
            self.target_animation_object = target
        self.animation_duration = duration
        self.animation_function = animation_function
        self.animation_object_difference = target - self.animation_object

    def update(self):
        if self.animation_fired:
            self.current_timestamp = (time.time() - self.begin_timestamp) * 100

            if self.animation_type == AnimationTypes.UNIDIRECTIONAL:
                self.begin_unidirectional_movement()
            if self.animation_type == AnimationTypes.PULSE:
                self.begin_pulsating_movement()
