from datetime import datetime
import json
import requests
from const import SceneTitles
from mesa import *
import pygame as pg


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-SemiBold.ttf")
        self.set_font_size(28)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


class mainTitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(32)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(25)
        self.set_text_color("black")
        self.set_text("予約内容確認")
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
        self.set_text("※まだ予約は完了していません。")
        self.set_color_as_parent()
        self.center_text()
        self.set_margin(1, 7)
        self.parent.add_element(self)


class titlebox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(80)
        self.set_background_color("#F3F3F3")
        self.set_margin(0, 10)
        self.title = mainTitle(self)
        self.title2 = subtitle(self)
        self.parent.add_element(self)


class whiteBox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(325)
        self.set_fixed_height(158)
        self.set_background_color("white")
        self.parent.add_element(self)


class kage(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(330)
        self.set_fixed_height(165)
        self.set_background_color("#E6E6E6")
        self.parent.add_element(self)
        self.border_left("#F3F3F3", 3)
        self.border_up("#F3F3F3", 3)


class yoyakutitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(40)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_text("【予約内容】")
        self.set_color_as_parent()
        self.set_margin(8, 7)
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
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "メーカー　　　　　：")
        self.text2 = yoyakutext2(self, f"{text}")
        self.parent.add_element(self)


class yoyakutextbox2(MesaStackHorizontal):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "機種名　　　　　　：")
        self.text2 = yoyakutext2(self, f"{text}")
        self.parent.add_element(self)


class yoyakutextbox3(MesaStackHorizontal):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル期間　　　：")
        self.text2 = yoyakutext2(self, f"{text}")
        self.parent.add_element(self)


class yoyakutextbox4(MesaStackHorizontal):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル開始日時　：")
        self.text2 = yoyakutext2(self, f"{text}")
        self.parent.add_element(self)


class yoyakutextbox5(MesaStackHorizontal):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.set_background_color("white")
        self.set_margin(20, 0)
        self.text1 = yoyakutext1(self, "レンタル終了日時　：")
        self.text2 = yoyakutext2(self, f"{text}")
        self.parent.add_element(self)


class tyuititle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text("【注意事項】")
        self.set_color_as_parent()
        self.set_margin(8, 3)
        self.parent.add_element(self)


class tyuitext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(21)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(11)
        self.set_text_color("#3C3C3C")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(15, 0)
        self.parent.add_element(self)


class tyuitext2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(17)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(11)
        self.set_text_color("#3C3C3C")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(15, 0)
        self.parent.add_element(self)


class tyuibox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(256)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 5)
        self.title = tyuititle(self)
        self.text1 = tyuitext(self, "・予約確定後の予約内容変更は一切出来ません。")
        self.text2 = tyuitext(self, "・PCの受け取り時間はレンタル開始日時の一時間前です。")
        self.text3 = tyuitext(self, "・PCの返却時間はレンタル終了日時の30分後までです。")
        self.text4 = tyuitext2(self, "・PCレンタル期間中の故障してしまった場合は、学校内で修")
        self.text7 = tyuitext2(self, "　理が可能な範囲内での過失であるときに限り、修理費用の")
        self.text8 = tyuitext(self, "　5000円を上限とした補償を受けることが可能です。")
        self.text5 = tyuitext2(self, "・修理が不可能な故障の場合、また貸出時と異なる状態で返")
        self.text9 = tyuitext(self, "　却された場合は修理費用全額をご負担いただきます。")
        self.text6 = tyuitext2(self, "・盗難や紛失が起こった場合、市場販売金額の100%をご請")
        self.text10 = tyuitext(self, "　求させていただきます。")
        self.parent.add_element(self)


class kakuteitext(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(325)
        self.set_fixed_height(45)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(11)
        self.set_text_color("#252525")
        self.set_text("予約内容と注意事項をご確認の上、お間違えなければ「 予約を確定する 」を押してください。")
        self.set_color_as_parent()
        self.set_margin(30, 3)
        self.parent.add_element(self)


class kakuteiButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(340)
        self.set_fixed_height(65)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(21)
        self.set_text_color("white")
        self.set_text("予約を確定する")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(40, 0)
        self.parent.add_element(self)


class kakuteibox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(120)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 0)
        self.title = kakuteitext(self)
        self.button = kakuteiButton(self)
        self.parent.add_element(self)


class henkoutext(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(335)
        self.set_fixed_height(42)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-SemiBold.ttf")
        self.set_font_size(10)
        self.set_text_color("#252525")
        self.set_text("※予約内容に変更がある場合はこちらからお戻りいただき、　内容の変更を行ってください。")
        self.set_color_as_parent()
        self.set_margin(33, 3)
        self.parent.add_element(self)


class henkouButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(340)
        self.set_fixed_height(48)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(14)
        self.set_text_color("white")
        self.set_text("予約内容を変更する")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(75, 0)
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        print("clicked, henkou")
        self.move_to_screen(SceneTitles.SceneRentalItemSelected)


class henkoubox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(200)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)
        self.title = henkoutext(self)
        self.button = henkouButton(self)
        self.parent.add_element(self)


class yoyakubox(MesaStackVertical):
    def __init__(self, parent, maker, name, jikan, start, end) -> None:
        super().__init__(parent)
        self.set_fixed_width(360)
        self.set_fixed_height(168)
        self.set_background_color("#F3F3F3")
        self.set_margin(5, 5)
        self.kage = kage(self)
        self.box = whiteBox(self.kage)
        self.title = yoyakutitle(self.box)
        self.text1 = yoyakutextbox1(self.box, maker)
        self.text2 = yoyakutextbox2(self.box, name)
        self.text3 = yoyakutextbox3(self.box, jikan)
        self.text4 = yoyakutextbox4(self.box, start)
        self.text5 = yoyakutextbox5(self.box, end)
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.title = titlebox(self)
        self.yoyaku = yoyakubox(self, None, None, None, None, None)
        self.tyui = tyuibox(self)
        self.title = kakuteitext(self)
        self.button = kakuteiButton(self)
        self.title = henkoutext(self)
        self.button2 = henkouButton(self)
        self.parent.add_element(self)

        self.structdata = None
        self.start = None
        self.end = None
        self.pcid = None
        self.userid = None
        self.rentalnum = None
        self.received = None
        self.returned = None

        self.core.eventsys.subscribe("RENTALSIGNAL", lambda data: self.get_data(data))
        self.button.set_signal(self.post_rental_information)

    def get_data(self, data):
        self.structdata = data[0]
        self.yoyaku.text1.text2.text = self.structdata.name
        self.yoyaku.text2.text2.text = self.structdata.maker

        diff = datetime.strptime(data[2], "%m-%d-%y %H:%M:%S") - datetime.strptime(
            data[1], "%m-%d-%y %H:%M:%S"
        )
        self.yoyaku.text3.text2.text = f"{diff}"

        self.start = data[1]
        self.end = data[2]
        self.pcid = data[3]
        self.rentalnum = data[5]
        self.received = data[6]
        self.returned = data[7]
        self.yoyaku.text4.text2.text = f"{self.start}"
        self.yoyaku.text5.text2.text = f"{self.end}"
        self.yoyaku.text1.text2.make_text_surface()
        self.yoyaku.text2.text2.make_text_surface()
        self.yoyaku.text3.text2.make_text_surface()
        self.yoyaku.text4.text2.make_text_surface()
        self.yoyaku.text5.text2.make_text_surface()
        self.yoyaku.text2.text2.make_text_surface()

    def post_rental_information(self):
        requests.post(
            f"http://renteckdb.site/rent/{self.rentalnum}/{self.pcid}/{self.userid}/{self.start}/{self.end}/{self.received}/{self.returned}"
        )
        self.core.info_tag.inform("レンタル成功。")
        self.move_to_screen(SceneTitles.SceneRentalItemList)


class ConfirmRentalScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.scrool = scroll(self.container)
        self.container.set_as_core()
        self.container.build()
