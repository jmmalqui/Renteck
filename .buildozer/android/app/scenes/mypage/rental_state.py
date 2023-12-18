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
        # self.set_signal(self.show_press)

    # def show_press(self):
    # self.move_to_screen("")


class mainTitle1(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(40)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text("現在のレンタル状況")
        self.set_color_as_parent()
        self.set_margin(5, 5)
        self.parent.add_element(self)


class whiteBox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(325)
        self.set_fixed_height(148)
        self.set_background_color("white")
        self.parent.add_element(self)


class kage(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(330)
        self.set_fixed_height(153)
        self.set_background_color("#E6E6E6")
        self.parent.add_element(self)
        self.border_left("#F3F3F3", 3)
        self.border_up("#F3F3F3", 3)


class yoyakutitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("#818181")
        self.set_text("20XX/XX/XX")
        self.set_color_as_parent()
        self.set_margin(14, 4)
        self.parent.add_element(self)


class yoyakutext1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(120)
        self.set_fixed_height(26)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class yoyakutext2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(26)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 0)
        self.parent.add_element(self)


class yoyakutextbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "メーカー　　　　　：")
        self.text2 = yoyakutext2(self, "レンタル中のPCのメーカ名")
        self.parent.add_element(self)


class yoyakutextbox2(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "機種名　　　　　　：")
        self.text2 = yoyakutext2(self, "レンタル中のPCの機種名")
        self.parent.add_element(self)


class yoyakutextbox3(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル期間　　　：")
        self.text2 = yoyakutext2(self, "xx時間")
        self.parent.add_element(self)


class yoyakutextbox4(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル開始日時　：")
        self.text2 = yoyakutext2(self, "20xx年xx月xx日 xx:xx")
        self.parent.add_element(self)


class yoyakutextbox5(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル終了日時　：")
        self.text2 = yoyakutext2(self, "20xx年xx月xx日 xx:xx")
        self.parent.add_element(self)


class yoyakubox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(360)
        self.set_fixed_height(168)
        self.set_background_color("#F3F3F3")
        self.set_margin(5, 5)
        self.kage = kage(self)
        self.box = whiteBox(self.kage)
        self.title = yoyakutitle(self.box)
        self.text1 = yoyakutextbox1(self.box)
        self.text2 = yoyakutextbox2(self.box)
        self.text2 = yoyakutextbox3(self.box)
        self.text2 = yoyakutextbox4(self.box)
        self.text2 = yoyakutextbox5(self.box)
        self.parent.add_element(self)


class henkyakuButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(182)
        self.set_fixed_height(52)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(15)
        self.set_text_color("white")
        self.set_text("返却済みにする")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(15, 0)
        self.parent.add_element(self)
        # self.set_signal(self.show_press)

    # def show_press(self):
    # self.move_to_screen("")


class uketoriButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(150)
        self.set_fixed_height(52)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(14)
        self.set_text_color("white")
        self.set_text("受け取り済みにする")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(0, 0)
        self.parent.add_element(self)


"""
受け取り済みボタンを押す前の返却ボタンの表示
class henkyakumae(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(182)
        self.set_fixed_height(52)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(15)
        self.set_text_color("#C3C3C3")
        self.set_text("返却済みにする")
        self.set_background_color("#818181")
        self.center_text()
        self.center_vertical()
        self.set_margin(15,0)
        self.parent.add_element(self)

"""

"""
受け取り済みボタンを一度押したらこっちに換える
class uketorizumi(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(150)
        self.set_fixed_height(52)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(15)
        self.set_text_color("#C3C3C3")
        self.set_text("受け取り済み")
        self.set_background_color("#818181")
        self.center_text()
        self.center_vertical()
        self.set_margin(0,0)
        self.parent.add_element(self)

"""

# どちらのボタンも押されたら履歴に移る
"""
レンタルしているPCがないときに表示
class NOrentaru(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(70)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-medium.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text("現在レンタルしているPCはありません")
        self.set_color_as_parent()
        self.set_margin(30,20)
        self.parent.add_element(self)

"""


class buttonbox(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.set_background_color("#F3F3F3")
        self.set_margin(10, 0)
        self.button1 = uketoriButton(self)
        self.button2 = henkyakuButton(self)
        self.parent.add_element(self)


class rentarubox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(300)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)
        self.title = mainTitle1(self)
        self.box = yoyakubox(self)
        self.button = buttonbox(self)
        # self.text=NOrenteru(self)
        self.parent.add_element(self)


class mainTitle2(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_fixed_height(40)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text("履歴")
        self.set_color_as_parent()
        self.set_margin(5, 5)
        self.parent.add_element(self)


class rirekititle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("#818181")
        self.set_text("20XX/XX/XX")
        self.set_color_as_parent()
        self.set_margin(14, 4)
        self.parent.add_element(self)


class rirekitextbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "メーカー　　　　　：")
        self.text2 = yoyakutext2(self, "レンタルしたPCのメーカ名")
        self.parent.add_element(self)


class rirekitextbox2(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "機種名　　　　　　：")
        self.text2 = yoyakutext2(self, "レンタルしたPCの機種名")
        self.parent.add_element(self)


class rirekitextbox3(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル期間　　　：")
        self.text2 = yoyakutext2(self, "xx時間")
        self.parent.add_element(self)


class rirekitextbox4(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル開始日時　：")
        self.text2 = yoyakutext2(self, "20xx年xx月xx日 xx:xx")
        self.parent.add_element(self)


class rirekitextbox5(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル終了日時　：")
        self.text2 = yoyakutext2(self, "20xx年xx月xx日 xx:xx")
        self.parent.add_element(self)


class rirekiwhitebox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(360)
        self.set_fixed_height(168)
        self.set_background_color("#F3F3F3")
        self.set_margin(5, 5)
        self.kage = kage(self)
        self.box = whiteBox(self.kage)
        self.title = rirekititle(self.box)
        self.text1 = rirekitextbox1(self.box)
        self.text1 = rirekitextbox2(self.box)
        self.text1 = rirekitextbox3(self.box)
        self.text1 = rirekitextbox4(self.box)
        self.text1 = rirekitextbox5(self.box)
        self.parent.add_element(self)


class rirekibox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(560)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)
        self.title = mainTitle2(self)
        self.box = rirekiwhitebox(self)
        self.box = rirekiwhitebox(self)
        self.box = rirekiwhitebox(self)
        # self.text=NOrenteru(self)
        self.parent.add_element(self)


class homeButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(360)
        self.set_fixed_height(70)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(13)
        self.set_text_color("white")
        self.set_text("ホームに戻る")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(105, 10)
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.box = rentarubox(self)
        self.box2 = rirekibox(self)
        self.button = homeButton(self)
        self.parent.add_element(self)


class RentalStateScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "レンタル状況")
        self.modoru = modoru(self.title)
        self.scrool = scroll(self.container)
        self.container.set_as_core()
        self.container.build()
