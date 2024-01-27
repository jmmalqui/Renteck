from mesa import *
import pygame as pg


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Bold.ttf")
        self.set_font_size(22)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        # self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)


class modoru(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(60)
        self.set_fixed_height(82)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Bold.ttf")
        self.set_font_size(25)
        self.set_text_color("black")
        self.set_text("＜")
        self.set_background_color("white")
        self.center_text()
        self.center_vertical()
        self.set_margin(5, 10)
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.move_to_screen("item-list")


class mainTitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(128)
        self.set_fixed_height(45)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text("こんにちは、")
        self.set_color_as_parent()
        self.set_margin(0, 1)
        self.parent.add_element(self)


class name(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(300)
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(33)
        self.set_text_color("black")
        self.set_text(f"something went wrong")
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)
        self.core.eventsys.subscribe("USERLOGIN", lambda data: self.update_text(data))

    def update_text(self, data):
        self.text = data
        self.make_text_surface()


class titlebox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(120)
        self.set_background_color("#F3F3F3")
        self.set_margin(7, 4)
        self.title = mainTitle(self)
        self.name = name(self)
        self.parent.add_element(self)


class whiteBox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(330)
        self.set_fixed_height(110)
        self.set_background_color("white")
        self.parent.add_element(self)


class kage(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(336)
        self.set_fixed_height(116)
        self.set_background_color("#E6E6E6")
        self.parent.add_element(self)
        self.border_left("#F3F3F3", 3)
        self.border_up("#F3F3F3", 3)


class subtitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(40)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_text("【お客様情報】")
        self.set_color_as_parent()
        self.set_margin(8, 8)
        self.parent.add_element(self)


class normaltext1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(115)
        self.set_fixed_height(26)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(14)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class normaltext2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(26)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class informationbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = normaltext1(self, "ペンネーム　　：")
        self.text2 = normaltext2(self, "入力されたペンネーム")
        self.parent.add_element(self)


class informationbox2(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = normaltext1(self, "メールアドレス：")
        self.text2 = normaltext2(self, "入力されたメールアドレス")
        self.parent.add_element(self)


class box1(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(600)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 20)
        self.title = titlebox(self)
        self.kage = kage(self)
        self.box = whiteBox(self.kage)
        self.title = subtitle(self.box)
        self.text1 = informationbox1(self.box)
        self.text2 = informationbox2(self.box)
        self.memo = imagebox(self)
        self.button = rentaruButton(self)
        self.button2 = logoutButton(self)
        self.parent.add_element(self)


class Image(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(130)
        self.set_fixed_width(130)
        self.set_image("res/memo.png")
        self.set_color_as_parent()
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()


class imagebox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(320)
        self.set_fixed_height(150)
        self.set_background_color("#F3F3F3")
        self.image = Image(self)
        self.set_margin(97, 15)
        self.parent.add_element(self)


class rentaruButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(330)
        self.set_fixed_height(53)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(17)
        self.set_text_color("white")
        self.set_text("レンタル状況確認")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(47, 0)
        self.parent.add_element(self)
        self.set_signal(self.goto_rentalstate)

    def goto_rentalstate(self):
        self.scene.manager.go_to("rentalstate")


class logoutButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(325)
        self.set_fixed_height(105)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(13)
        self.set_text_color("white")
        self.set_text("ログアウト")
        self.set_background_color("#818181")
        self.center_text()
        self.center_vertical()
        self.set_margin(95, 30)
        self.parent.add_element(self)
        self.set_signal(self.logout)

    def logout(self):
        self.move_to_screen("login")


class MyPageEntryScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "マイページ")
        self.modoru = modoru(self.title)
        self.box = box1(self.container)
        self.set_background_color("#F3F3F3")
        self.container.set_as_core()
        self.container.build()
