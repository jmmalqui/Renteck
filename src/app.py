import mesa
import pygame as pg
from scenes.entry.entry_scene import EntryScene
from scenes.registration.login import LoginScene
from scenes.display_item.display_items_scene import DisplayItemsScene
from scenes.item_descriptor.item_descriptor_scene import ItemDescriptorScene
from scenes.registration.new_registration import NewRegistrationScene
from scenes.registration.registration_success import RegistrationSuccessScene
from scenes.registration.hontouroku1 import RealRegistration
from scenes.rental.period import RentalPeriodScene
from scenes.rental.rental_success import RentalSuccess


class Renteck(mesa.MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Renteck")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.entry = EntryScene(self, "entry", self.scene_manager)
        self.login = LoginScene(self, "login", self.scene_manager)
        self.registration = NewRegistrationScene(self, "new-reg", self.scene_manager)
        self.registration_success = RegistrationSuccessScene(
            self, "reg-success", self.scene_manager
        )
        self.real_regist = RealRegistration(self, "real-reg", self.scene_manager)
        self.item_list = DisplayItemsScene(self, "item-list", self.scene_manager)
        self.item_descriptor = ItemDescriptorScene(
            self, "item-descriptor", self.scene_manager
        )
        self.rental_period = RentalPeriodScene(self, "rental-set", self.scene_manager)
        self.rental_success = RentalSuccess(self, "rental-success", self.scene_manager)
        self.scene_manager.set_init_scene("entry")
