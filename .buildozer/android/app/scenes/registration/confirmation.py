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


class mainTitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(32)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(25)
        self.set_text_color("black")
        self.set_text("入力内容確認")
        self.set_color_as_parent()
        self.center_text()
        self.parent.add_element(self)


class subtitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("red")
        self.set_text("※まだ登録は完了していません。")
        self.set_color_as_parent()
        self.center_text()
        self.set_margin(1, 7)
        self.parent.add_element(self)


class titlebox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(70)
        self.set_background_color("#F3F3F3")
        self.set_margin(0, 5)
        self.title = mainTitle(self)
        self.title2 = subtitle(self)
        self.parent.add_element(self)


class normaltext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(16)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class textbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(50)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 0)
        self.text1 = normaltext(self, "お客様の登録情報を表示しています。")
        self.text2 = normaltext(self, "以下の内容にお間違いがなければ「会員登録をする」を押してください。")
        self.parent.add_element(self)


class normaltext2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(110)
        self.set_fixed_height(31)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("#3C3C3C")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 2)
        self.parent.add_element(self)


class mailtext(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(250)
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("black")
        self.set_text("入力されたメールアドレスを表示")
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class nametext(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(250)
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("black")
        self.set_text("入力されたニックネームを表示")
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class borderbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(350)
        self.set_fixed_height(65)
        self.set_background_color("#F3F3F3")
        self.parent.add_element(self)
        self.set_margin(15, 10)
        self.border_down("#3C3C3C", 1.5)


class mailbox(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(34)
        self.set_background_color("#F3F3F3")
        self.set_margin(7, 8)
        self.text1 = normaltext2(self, "メールアドレス")
        self.text2 = mailtext(self)
        self.parent.add_element(self)


class namebox(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(34)
        self.set_background_color("#F3F3F3")
        self.set_margin(7, 8)
        self.text1 = normaltext2(self, "ニックネーム")
        self.text2 = nametext(self)
        self.parent.add_element(self)


class informationbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(150)
        self.set_background_color("#F3F3F3")
        self.box1 = borderbox(self)
        self.mail = mailbox(self.box1)
        self.box2 = borderbox(self)
        self.name = namebox(self.box2)
        self.parent.add_element(self)
        self.set_margin(5, 7)


class kakuteiButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(175)
        self.set_fixed_height(48)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(15)
        self.set_text_color("white")
        self.set_text("会員登録をする")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(10, 0)
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.move_to_screen("totalsuccess", False)


class modoruButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(160)
        self.set_fixed_height(48)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(15)
        self.set_text_color("white")
        self.set_text("戻る")
        self.set_background_color("#818181")
        self.center_text()
        self.center_vertical()
        self.set_margin(0, 0)
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.move_to_screen("real-reg")


class buttonbox(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(100)
        self.set_background_color("#F3F3F3")
        self.set_margin(18, 0)
        self.button1 = modoruButton(self)
        self.button2 = kakuteiButton(self)
        self.parent.add_element(self)


class UserInfoConfirmationScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "会員本登録")
        self.title = titlebox(self.container)
        self.text = textbox(self.container)
        self.box = informationbox(self.container)
        self.button = buttonbox(self.container)
        self.set_background_color("#F3F3F3")
        self.container.set_as_core()
        self.container.build()
