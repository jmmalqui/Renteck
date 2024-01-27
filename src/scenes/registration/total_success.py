from const import SceneTitles
from mesa import *
import pygame as pg

sentence1 = "この度は「Renteck」にご登録いただきありがとうございます。" "引き続きご利用の方は下のボタンからトップページへお戻りください。"


class TotalSuccessScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F3F3F3")
        self.container = MesaStackVertical(self)
        self.title1 = Title1(self.container, "Renteck")  # 上部ラベル
        self.box = box(self.container)
        self.MyButton1 = MyButton1(self.container, "トップに戻る", "white", "black")
        self.container.set_as_core()
        self.container.build()


class Title1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(28)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


# 画像(予約が完了しました)
class Image1(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(140)
        self.set_margin(30, 0)
        self.set_background_color("#F3F3F3")
        self.set_image("res/hontouroku2.PNG")
        self.center_element()
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()
        return super().late_init()


# テキスト(sentence1)
class CustomText1(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_height(height)
        self.set_fixed_width(360)
        self.set_margin(20, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("#818181")
        self.set_text(text)
        self.set_background_color("#F3F3F3")
        self.center_text()
        self.parent.add_element(self)


# トップに戻る
class MyButton1(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(47)
        self.set_margin(70, 0)
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
        self.manager.go_to(SceneTitles.SceneLogin)


class box(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.image1 = Image1(self)
        self.text1 = CustomText1(self, sentence1, 60)
        self.set_width_as_parent()
        self.set_fixed_height(300)
        self.set_color_as_parent()
        self.set_margin(0, 35)
        self.set_background_color("#F3F3F3")
        self.parent.add_element(self)
