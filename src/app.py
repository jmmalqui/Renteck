import mesa
import pygame as pg
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
from scenes.rental.confirm import ConfirmRentalScene

from scenes.mypage.mypage_entry import MyPageEntryScene
from scenes.mypage.rental_state import RentalStateScene


from const import APPSIZE
from const import SceneTitles


class Renteck(mesa.MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Renteck")
        self.set_rendering_flags(pg.SCALED, pg.DOUBLEBUF)
        self.set_display_size(APPSIZE[0], APPSIZE[1])
        self.set_clock(600)
        self.userid = None
        self.login = LoginScene(self, SceneTitles.SceneLogin, self.scene_manager)

        self.mypageentry = MyPageEntryScene(
            self, SceneTitles.SceneMyPageEntry, self.scene_manager
        )
        self.rentalstate = RentalStateScene(
            self, SceneTitles.SceneRentalState, self.scene_manager
        )
        self.registration = NewRegistrationScene(
            self, SceneTitles.SceneNewRegistration, self.scene_manager
        )
        self.registration_success = RegistrationSuccessScene(
            self, SceneTitles.SceneRegistrationSuccesful, self.scene_manager
        )
        self.real_regist = RealRegistration(
            self, SceneTitles.SceneRealRegistration, self.scene_manager
        )
        self.dataconfirm = UserInfoConfirmationScene(
            self, SceneTitles.SceneUserInfoConfirmation, self.scene_manager
        )
        self.totalsucess = TotalSuccessScene(
            self, SceneTitles.SceneUserInfoAndRegistrationSuccess, self.scene_manager
        )
        self.item_list = DisplayItemsScene(
            self, SceneTitles.SceneRentalItemList, self.scene_manager
        )
        self.item_descriptor = ItemDescriptorScene(
            self, SceneTitles.SceneRentalItemDescription, self.scene_manager
        )
        self.rental_period = RentalPeriodScene(
            self, SceneTitles.SceneRentalItemSelected, self.scene_manager
        )
        self.rental_success = RentalSuccess(
            self, SceneTitles.SceneRentalItemRentalSuccess, self.scene_manager
        )
        self.confirm = ConfirmRentalScene(
            self, SceneTitles.ConfirmRental, self.scene_manager
        )
        self.scene_manager.set_init_scene(SceneTitles.SceneLogin)
