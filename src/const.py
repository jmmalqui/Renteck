import enum
import os

PATH = os.path.abspath(".") + "/src/"
if "ANDROID_ARGUMENT" in os.environ:
    PATH = os.path.abspath(".") + "/"
APPSIZE = [1080 // 3, 2160 // 3]


class SceneTitles(enum.Enum):
    SceneLogin = enum.auto()
    SceneMyPageEntry = enum.auto()
    SceneRentalState = enum.auto()
    SceneNewRegistration = enum.auto()
    SceneRegistrationSuccesful = enum.auto()
    SceneRealRegistration = enum.auto()
    SceneUserInfoConfirmation = enum.auto()
    SceneUserInfoAndRegistrationSuccess = enum.auto()
    SceneRentalItemList = enum.auto()
    SceneRentalItemDescription = enum.auto()
    SceneRentalItemSelected = enum.auto()
    SceneRentalItemRentalSuccess = enum.auto()
    ConfirmRental = enum.auto()
