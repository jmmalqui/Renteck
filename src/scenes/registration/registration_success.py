from mesa import *
import pygame as pg

sentence1 = (
    "※まだ会員登録は完了してません。\n\n"
    "ご登録いただいたメールアドレス宛に、本登録を行うためのメールをお送りいたしました。"
    "メール本文に記載されているURLから会員登録を完了させてください。\n\n"
    "※本登録手続きメールが届かない場合、入力したメールアドレスが間違っている可能性があります。"
    "再度、最初から新規会員登録を行ってください"
)


class RegistrationSuccessScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#E6E6E6")
        self.container = MesaStackVertical(self)
        self.title1 = Title1(self.container, "仮登録完了")  # 上部ラベル
        self.title2 = Title2(self.container, "仮登録が完了しました．")
        self.text1 = CustomText1(self.container, sentence1, 200)
        self.MyButton1 = GoToTopPage(self.container, "トップページへ", "white", "black")
        self.container.set_as_core()
        self.container.build()


# ラベル（上部）
class Title1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


# テキスト（仮登録が完了しました）
class Title2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(120)
        self.set_margin(50, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


# テキスト（sentence1）
class CustomText1(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        # self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_fixed_width(360)
        self.set_margin(20, 30)
        # self.set_margin(0,)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


class GoToTopPage(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(70)
        self.set_margin(70, 10)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(25)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.move_to_screen("entry")
