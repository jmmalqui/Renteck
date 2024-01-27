import json
import requests
from mesa import *
import pygame as pg
import datetime

from mesa.info_tag.tag import InfoTagLevels


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
        self.set_font_size(21)
        self.set_text_color("black")
        self.set_text("レンタル期間選択")
        self.border("#DDF2FD", 2)
        self.set_color_as_parent()
        self.center_text()
        self.parent.add_element(self)


class textbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(75)
        self.set_color_as_parent()
        self.title = mainTitle(self)
        self.text = NormalText1(self)
        self.parent.add_element(self)
        self.set_margin(0, 12)


class NormalText1(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(18)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text("レンタル開始日時と終了日時を選択してください")
        self.set_color_as_parent()
        self.center_text()
        self.set_margin(0, 2)
        # self.center_vertical()
        self.parent.add_element(self)


class NormalText2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(160)
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(3, 2)
        self.parent.add_element(self)


class hinichitext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(23)
        self.set_fixed_height(33)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(0, 6)
        self.parent.add_element(self)


class yearBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(37)
        self.set_fixed_width(80)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.set_margin(3, 2)
        self.parent.add_element(self)


class monthBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(37)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.set_margin(2, 2)
        self.parent.add_element(self)


class dayBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(37)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.set_margin(2, 2)
        self.parent.add_element(self)


class timeBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(37)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.set_margin(2, 2)
        self.parent.add_element(self)


class inputbox(MesaStackHorizontal):
    def __init__(self, parent, yoko, tate) -> None:
        super().__init__(parent)
        self.set_fixed_height(70)
        self.set_width_as_parent()
        self.set_background_color("#F3F3F3")
        self.yearbox = yearBox(self)
        self.yeartext = hinichitext(self, "年")
        self.month = monthBox(self)
        self.yeartext = hinichitext(self, "月")
        self.day = dayBox(self)
        self.yeartext = hinichitext(self, "日")
        self.time = timeBox(self)
        self.yeartext = hinichitext(self, "時")
        self.parent.add_element(self)
        self.set_margin(yoko, tate)


class startbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(400)
        self.set_fixed_height(82)
        self.set_color_as_parent()
        self.start = NormalText2(self, "● レンタル開始日時")
        self.nichiji = inputbox(self, 1, 1)
        self.parent.add_element(self)
        self.set_margin(10, 8)


class finalbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(400)
        self.set_fixed_height(80)
        self.set_color_as_parent()
        self.start = NormalText2(self, "● レンタル終了日時")
        self.nichiji = inputbox(self, 1, 1)
        self.parent.add_element(self)
        self.set_margin(10, 5)


class kakuninButton(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(357)
        self.set_fixed_height(118)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(19)
        self.set_text_color("white")
        self.set_text("確認画面へ")
        self.set_background_color("black")
        self.center_text()
        self.center_vertical()
        self.set_margin(84, 30)
        self.parent.add_element(self)


class namisenImage(MesaImage):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_height(60)
        self.set_fixed_width(30)
        self.pathimage = image
        self.set_image(image)
        self.set_color_as_parent()
        self.center_vertical()
        self.center_element()
        self.set_margin(0, 0)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()


class imagebox(MesaStackVertical):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(60)
        self.set_background_color("#F3F3F3")
        self.image = namisenImage(self, image)
        self.set_margin(170, 0)
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.text1 = textbox(self)
        self.box1 = startbox(self)
        self.image = imagebox(self, "res/namisen.png")
        self.box2 = finalbox(self)
        self.button = kakuninButton(self)
        self.parent.add_element(self)
        self.button.set_signal(self.show_press)
        self.core.eventsys.subscribe("DATATRANSFER", lambda data: self.get_data(data))
        self.data = None

    def get_data(self, data):
        self.data = data

    def show_press(self):
        can_cotinue = True
        begin = [
            self.box1.nichiji.yearbox.get_written_text(),
            self.box1.nichiji.month.get_written_text(),
            self.box1.nichiji.day.get_written_text(),
            self.box1.nichiji.time.get_written_text(),
        ]
        end = [
            self.box2.nichiji.yearbox.get_written_text(),
            self.box2.nichiji.month.get_written_text(),
            self.box2.nichiji.day.get_written_text(),
            self.box2.nichiji.time.get_written_text(),
        ]
        try:
            begintime = datetime.datetime(
                year=int(begin[0]),
                month=int(begin[1]),
                day=int(begin[2]),
                hour=int(begin[3]),
            )
        except ValueError as e:
            self.core.info_tag.inform(f"適切な日時ではありません:  {e}", InfoTagLevels.CRITICAL)
            can_cotinue = False

        try:
            endtime = datetime.datetime(
                year=int(end[0]), month=int(end[1]), day=int(end[2]), hour=int(end[3])
            )

        except ValueError as e:
            self.core.info_tag.inform(f"適切な日時ではありません: {e}", InfoTagLevels.CRITICAL)
            can_cotinue = False

        for entry in begin:
            if not entry.isnumeric():
                self.core.info_tag.inform("数字だけ入力してください。", InfoTagLevels.CRITICAL)
                can_cotinue = False
        for entry in end:
            if not entry.isnumeric():
                self.core.info_tag.inform("数字だけ入力してください。", InfoTagLevels.CRITICAL)
                can_cotinue = False

        if begin.count("") != 0 or end.count("") != 0:
            self.core.info_tag.inform("全てのボックスを埋めてください", InfoTagLevels.CRITICAL)
            can_cotinue = False
        if can_cotinue:
            getid = requests.request("GET", f"http://renteckdb.site/uid/{self.data[0]}")
            getidjson = json.loads(getid.content)
            userid = getidjson["id"]
            pcid = self.data[1]
            rentalnumber = self.data[2]
            returned = 0
            received = 1
            start = begintime.strftime("%Y-%m-%d %H:%M:%S")
            end = endtime.strftime("%Y-%m-%d %H:%M:%S")
            requests.post(
                f"http://renteckdb.site/rent/{rentalnumber}/{pcid}/{userid}/{start}/{end}/{received}/{returned}"
            )
            self.core.eventsys.emit("RENTALSIGNAL", None)
            self.core.info_tag.inform("レンタル成功。")
            self.move_to_screen("rental-success", False)


class RentalPeriodScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F3F3F3")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.scroll = scroll(self.container)

        self.container.set_as_core()
        self.container.build()
