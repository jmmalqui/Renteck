from mesa import *
import pygame as pg

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


class CustomBox(MesaStackVertical):
    def __init__(self, parent, width, height, color) -> None:
        super().__init__(parent)
        self.set_fixed_width(width)
        self.set_fixed_height(height)
        self.set_background_color(color)
        self.parent.add_element(self)


class kage(MesaStackVertical):
    def __init__(self, parent, width, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(width)
        self.set_fixed_height(height)
        self.set_background_color("#E6E6E6")
        self.parent.add_element(self)
        self.border_left("#E6E6E6", 7)
        self.border_up("#E6E6E6", 7)
        self.set_margin(9, 5)


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


class imagebox(MesaStackVertical):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_width(130)
        self.set_fixed_height(130)
        self.set_background_color("white")
        self.image = pcImage(self, image)
        self.parent.add_element(self)


class PCname1(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.parent.add_element(self)


class PCname2(MesaTextLabel):
    def __init__(self, parent, text, size, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(size)
        self.set_text_color("black")
        self.set_text(text)
        self.border_left("black", 4)
        self.set_background_color("white")
        self.parent.add_element(self)


class PCtitle1(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = PCname1(self, "  Microsoft", 25)
        self.pcname2 = PCname2(self, "  Surface Laptop Go2", 17, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class PCtitle2(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(50)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = PCname1(self, "  Lenovo", 25)
        self.pcname2 = PCname2(self, "  IdeaPad Slim 370i", 17, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class PCtitle3(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(50)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = PCname1(self, "  HP", 25)
        self.pcname2 = PCname2(self, "   Spectre x360 6F8L0PA-AAAB", 13, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class PCtitle4(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(50)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = PCname1(self, "  dynabook", 25)
        self.pcname2 = PCname2(self, "  C7 P2C7VBEL", 16, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class PCtitle5(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(50)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.pcname1 = PCname1(self, "  ASUS", 25)
        self.pcname2 = PCname2(self, "   TUF Dash F15 FX517ZC", 14, 25)
        self.buttom = seemore(self)
        self.border_left("black", 4)
        self.parent.add_element(self)
        self.set_margin(5, 12)


class GoIntoDescription(MesaButtonText):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(115)
        self.set_fixed_height(45)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("white")
        self.set_text(text)
        self.set_background_color("black")
        self.center_text()
        self.set_signal(self._signal)

        self.parent.add_element(self)
        print(self)

    def _signal(self):
        self.move_to_screen("item-descriptor")


class kariBox(MesaStackVertical):
    def __init__(self, parent, width, height, color) -> None:
        super().__init__(parent)
        self.set_fixed_width(width)
        self.set_fixed_height(height)
        self.set_background_color(color)
        self.parent.add_element(self)


class seemore(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.vpanel = kariBox(self, 59, 40, "white")
        self.button = GoIntoDescription(self, " ▶ SEE MORE ")
        self.parent.add_element(self)
        self.set_margin(13, 8)


class inbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.image = imagebox(self, "res/pc1.png")
        self.pcname = PCtitle1(self)
        self.parent.add_element(self)
        self.set_margin(3, 2)


class inbox2(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.image = imagebox(self, "res/pc2.png")
        self.pcname = PCtitle2(self)
        self.parent.add_element(self)
        self.set_margin(3, 2)


class inbox3(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.image = imagebox(self, "res/pc3.png")
        self.pcname = PCtitle3(self)
        self.parent.add_element(self)
        self.set_margin(3, 2)


class inbox4(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.image = imagebox(self, "res/pc4.png")
        self.pcname = PCtitle4(self)
        self.parent.add_element(self)
        self.set_margin(3, 2)


class inbox5(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("white")
        self.image = imagebox(self, "res/pc5.png")
        self.pcname = PCtitle5(self)
        self.parent.add_element(self)
        self.set_margin(3, 2)


class maru(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(10)
        self.set_fixed_height(10)
        self.set_background_color("#AAAAAA")
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.kage1 = kage(self, 358, 145)
        self.box1 = CustomBox(self.kage1, 335, 130, "white")
        self.kage2 = kage(self, 358, 145)
        self.box2 = CustomBox(self.kage2, 335, 130, "white")
        self.kage3 = kage(self, 358, 145)
        self.box3 = CustomBox(self.kage3, 335, 130, "white")
        self.kage4 = kage(self, 358, 145)
        self.box4 = CustomBox(self.kage4, 335, 130, "white")
        self.kage5 = kage(self, 358, 145)
        self.box5 = CustomBox(self.kage5, 335, 130, "white")
        self.inbox1 = inbox1(self.box1)
        # self.maru=maru(self.box1)
        self.inbox2 = inbox2(self.box2)
        self.inbox3 = inbox3(self.box3)
        self.inbox4 = inbox4(self.box4)
        self.inbox5 = inbox5(self.box5)
        self.parent.add_element(self)


class DisplayItemsScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F3F3F3")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.go_back = GoBackButton(self.title, "<", "black", "white")
        self.container.set_as_core()
        self.scroll = scroll(self.container)
        self.container.build()

    def update(self):
        self.title.set_text("Renteck " + self.previous_scene)
        for event in self.get_events():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.manager.return_to_previous_scene()
        return super().update()
