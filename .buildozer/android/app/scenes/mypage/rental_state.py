from datetime import datetime
import json
import requests
from mesa import *
import pygame as pg

from mesa.info_tag.tag import InfoTagLevels


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
        print("here")
        self.move_to_screen("mypageentry")


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
        self.set_text("未受取")
        self.set_text_color("lightred")
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
        self.text2 = yoyakutextbox3(self.box, jikan)
        self.text2 = yoyakutextbox4(self.box, start)
        self.text2 = yoyakutextbox5(self.box, end)
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


class rekishibox(MesaStackVertical):
    def __init__(
        self, parent, maker, name, jikan, start, end, rentalnum, userid
    ) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(200)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)
        self.rentalnum = rentalnum
        self.userid = userid
        self.box = yoyakubox(self, maker, name, jikan, start, end)
        self.box.title.text = "返却済"
        self.box.title.text_color = "lightblue"
        self.box.title.make_text_surface()
        self.parent.add_element(self)


class rentarubox(MesaStackVertical):
    def __init__(
        self, parent, maker, name, jikan, start, end, rentalnum, userid
    ) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(250)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)
        self.rentalnum = rentalnum
        self.userid = userid
        self.box = yoyakubox(self, maker, name, jikan, start, end)
        self.button = buttonbox(self)
        self.button.button1.set_signal(self.uketori)
        self.button.button2.set_signal(self.henkyaku)
        self.parent.add_element(self)

    def uketori(self):
        self.box.title.text = "受取済み"
        self.box.title.text_color = "lightgreen"
        self.box.title.make_text_surface()

    def henkyaku(self):
        req = requests.request(
            "GET",
            f"http://renteckdb.site/update_rental_status/{self.userid}/{self.rentalnum}",
        )
        self.box.title.text = "返却済"
        self.box.title.text_color = "lightgreen"
        self.box.title.make_text_surface()
        self.box.set_background_color([200, 0, 0])
        self.box.build()


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
        self.set_fixed_height(800)
        self.set_background_color("#F3F3F3")
        self.set_margin(15, 10)

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
        self.set_signal(self.gohome)

    def gohome(self):
        self.move_to_screen("item-list", False)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.title = mainTitle1(self)
        self.rentaruboxxes = []
        self.userid = None
        self.core.eventsys.subscribe("USERLOGIN", lambda data: self.load_user(data))
        self.core.eventsys.subscribe("RENTALSIGNAL", lambda data: self.REBUILD(data))

        self.button = homeButton(self)
        self.title2 = mainTitle2(self)
        self.rekishiboxxes = []
        self.enable_scrolling()
        self.parent.add_element(self)

    def late_init(self):
        self.REBUILD(None)

    def REBUILD(self, data: None):
        self.elements = []
        self.title = mainTitle1(self)
        self.get_rentaru_boxxes()
        self.button = homeButton(self)
        self.title2 = mainTitle2(self)
        self.get_rekishi_boxxes()
        self.parent.build()

    def load_user(self, data):
        getid = requests.request("GET", f"http://renteckdb.site/uid/{data}")
        jsonid = json.loads(getid.content)
        self.userid = jsonid["id"]
        self.REBUILD(None)

    def get_rentaru_boxxes(self):
        self.rentaruboxxes = []
        getdata = requests.request(
            "GET", f"http://renteckdb.site/rstatus/{self.userid}/0"
        )
        jsondata = json.loads(getdata.content)
        if "error" in jsondata:
            return
        for entry in jsondata:
            diff = datetime.strptime(
                entry["enddata"], "%a, %d %b %Y %H:%M:%S %Z"
            ) - datetime.strptime(entry["startdata"], "%a, %d %b %Y %H:%M:%S %Z")
            self.rentaruboxxes.append(
                rentarubox(
                    self,
                    entry["manufacturer"],
                    entry["model"],
                    f"{diff}",
                    entry["startdata"],
                    entry["enddata"],
                    entry["rentalnum"],
                    entry["userid"],
                )
            )

    def get_rekishi_boxxes(self):
        self.rekishiboxxes = []
        getdata = requests.request(
            "GET", f"http://renteckdb.site/rstatus/{self.userid}/1"
        )
        jsondata = json.loads(getdata.content)
        if "error" in jsondata:
            self.core.info_tag.inform("歴史は見つかりませんでした", InfoTagLevels.ALERT)
            self.title2.text = "歴史なし"
            return
        else:
            for entry in jsondata:
                diff = datetime.strptime(
                    entry["enddata"], "%a, %d %b %Y %H:%M:%S %Z"
                ) - datetime.strptime(entry["startdata"], "%a, %d %b %Y %H:%M:%S %Z")

                self.rentaruboxxes.append(
                    rekishibox(
                        self,
                        entry["manufacturer"],
                        entry["model"],
                        f"{diff}",
                        entry["startdata"],
                        entry["enddata"],
                        entry["rentalnum"],
                        entry["userid"],
                    )
                )


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
