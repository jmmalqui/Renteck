import json
from const import SceneTitles
from mesa import *
import pygame as pg
import requests
from utils.goback_button import GoBackButton


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(30)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


class pcImage(MesaImage):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_height(130)
        self.set_fixed_width(130)
        self.pathimage = image
        self.set_image(image)
        self.set_color_as_parent()
        self.center_vertical()
        self.center_element()
        self.set_margin(16, 16)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()


class ManufacturerLabel(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_margin(5, 0)
        self.set_background_color("white")
        self.parent.add_element(self)


class PCNameLabel(MesaTextLabel):
    def __init__(self, parent, text, size, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(size)
        self.set_text_color("black")
        self.set_text(text)
        self.set_margin(5, 0)
        self.set_background_color("white")
        self.parent.add_element(self)


class PCtitle(MesaStackVertical):
    def __init__(self, parent, name, man) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = ManufacturerLabel(self, man, 30)
        self.pcname2 = PCNameLabel(self, name, 20, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class GoIntoDescription(MesaButtonText):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(115)
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("white")
        self.set_text(text)
        self.set_background_color("black")
        self.center_text()

        self.parent.add_element(self)


class seemore(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("white")
        self.button = GoIntoDescription(self, " ▶ SEE MORE ")
        self.parent.add_element(self)
        self.set_margin(13, 8)


class RentalItem(MesaStackHorizontal):
    def __init__(self, parent, id, name, manufacturer) -> None:
        super().__init__(parent)
        self.name = name
        self.manufacturer = manufacturer
        self.itemid = id
        self.set_fixed_width(358)
        self.set_fixed_height(130)
        self.set_background_color("white")

        self.image = pcImage(self, f"res/pc{id}.png")
        self.pcname = PCtitle(self, self.name, self.manufacturer)
        self.set_margin(3, 2)
        self.pcname.buttom.button.set_signal(self.item_selected)
        self.parent.add_element(self)

    def item_selected(self):
        self.core.eventsys.emit(
            "ITEMSELECTED",
            [self.itemid, self.image.pathimage, self.name, self.manufacturer],
        )
        self.move_to_screen(SceneTitles.SceneRentalItemDescription)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.items = self.get_items()
        for item in self.items:
            manufacturer = self.items[item]["manufacturer"]
            model = self.items[item]["model"]
            self.item = RentalItem(self, item, model, manufacturer)

        self.parent.add_element(self)

    def get_items(self):
        req = requests.request("GET", "http://renteckdb.site/products")
        return json.loads(req.content)


class GoToMyPageButton(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_fixed_height(60)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.scene.manager.go_to(SceneTitles.SceneMyPageEntry)


class DisplayItemsScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F3F3F3")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.go_back = GoToMyPageButton(self.title, "<", "black", "white")
        self.scroll = scroll(self.container)
        self.container.set_as_core()

        self.container.build()

    def update(self):
        for event in self.get_events():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.manager.return_to_previous_scene()
        return super().update()
