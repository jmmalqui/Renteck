import mesa
import pygame as pg
from scenes.entry.entry_scene import EntryScene

from scenes.registration.login import LoginScene

from scenes.display_item.display_items_scene import DisplayItemsScene

from scenes.item_descriptor.item_descriptor_scene import ItemDescriptorScene

from scenes.registration.new_registration import NewRegistrationScene
from scenes.registration.registration_success import RegistrationSuccessScene
from scenes.registration.hontouroku1 import RealRegistration
from scenes.registration.confirmation import UserInfoConfirmationScene
from scenes.registration.total_success import TotalSuccessScene


from scenes.rental.period import RentalPeriodScene
from scenes.rental.rental_success import RentalSuccess

from scenes.mypage.mypage_entry import MyPageEntryScene
from scenes.mypage.rental_state import RentalStateScene


from const import APPSIZE


class Renteck(mesa.MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Renteck")
        self.set_rendering_flags(pg.SCALED, pg.DOUBLEBUF)
        self.set_display_size(APPSIZE[0], APPSIZE[1])
        # self.set_background_color("orange")
        self.set_clock(600)
        self.entry = EntryScene(self, "entry", self.scene_manager)
        self.login = LoginScene(self, "login", self.scene_manager)

        self.mypageentry = MyPageEntryScene(self, "mypageentry", self.scene_manager)
        self.rentalstate = RentalStateScene(self, "rentalstate", self.scene_manager)
        self.registration = NewRegistrationScene(self, "new-reg", self.scene_manager)
        self.registration_success = RegistrationSuccessScene(
            self, "reg-success", self.scene_manager
        )
        self.real_regist = RealRegistration(self, "real-reg", self.scene_manager)
        self.dataconfirm = UserInfoConfirmationScene(
            self, "userinfoconfirm", self.scene_manager
        )
        self.totalsucess = TotalSuccessScene(self, "totalsuccess", self.scene_manager)
        self.item_list = DisplayItemsScene(self, "item-list", self.scene_manager)
        self.item_descriptor = ItemDescriptorScene(
            self, "item-descriptor", self.scene_manager
        )
        self.rental_period = RentalPeriodScene(self, "rental-set", self.scene_manager)
        self.rental_success = RentalSuccess(self, "rental-success", self.scene_manager)
        self.scene_manager.set_init_scene("entry")

        self.debugfont = pg.font.SysFont("Arial", 30)
        self.sruf = self.debugfont.render(
            f"{pg.display.get_window_size()}", True, "red"
        )

    def render(self):
        self.sruf = self.debugfont.render(
            f"FPS:{self.clock.get_fps():.2f}", True, "red"
        )
        self.display.blit(self.sruf, [20, 20])
