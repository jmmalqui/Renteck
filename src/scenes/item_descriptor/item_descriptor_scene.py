import json
import requests
from const import SceneTitles
from mesa import *
import pygame as pg

from utils.goback_button import GoBackButton


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)

        self.set_width_as_display()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(30)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


class PCname1(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(23)
        self.set_text_color("black")
        self.set_background_color("#F3F3F3")
        self.set_text("Microsoft")
        self.parent.add_element(self)


class PCname2(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(125)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(30)
        self.set_text_color("black")
        self.set_background_color("#F3F3F3")
        self.set_text("Surface Laptop Go2")
        self.parent.add_element(self)


class PCtitle(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(140)
        self.set_color_as_parent()
        self.set_background_color("#F3F3F3")
        self.pcname1 = PCname1(self)
        self.pcname2 = PCname2(self)
        self.parent.add_element(self)
        self.set_margin(7, 10)


class pcImage(MesaImage):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_height(450)
        self.set_fixed_width(290)
        self.pathimage = image
        self.set_image(image)
        self.set_color_as_parent()
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()


class imagebox(MesaStackVertical):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_width(370)
        self.set_fixed_height(330)
        self.set_background_color("#F3F3F3")
        self.image = pcImage(self, image)
        self.set_margin(35, 6)
        self.parent.add_element(self)


class rentarutext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(170)
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.border("black", 2)
        self.set_background_color("#F3F3F3")
        self.center_text()
        self.set_margin(10, 5)
        self.parent.add_element(self)


class rentarutext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(170)
        self.set_fixed_height(55)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.border("black", 2)
        self.set_background_color("#F3F3F3")
        self.center_text()
        self.set_margin(10, 7)
        self.parent.add_element(self)


class daisu(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(270)
        self.set_fixed_height(73)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(17)
        self.set_text_color("black")
        self.set_text("残り　　台")
        self.set_background_color("#F3F3F3")
        self.set_margin(90, 16)
        self.center_text()
        self.parent.add_element(self)


class NormalText(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(20)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(2, 0)
        # self.center_text()
        # self.center_vertical()
        self.parent.add_element(self)


class number(MesaTextLabel):
    def __init__(self, parent, number) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(27)
        self.set_text_color("black")
        self.set_text(number)
        self.set_background_color("#00000000")
        self.set_margin(0, 3)
        self.center_text()
        self.parent.add_element(self)


class setumei(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(300)
        self.set_background_color("#F3F3F3")
        self.text1 = NormalText(self, "本体サイズ 　　:  278.2mm×206.2mm×15.7mm")
        self.text2 = NormalText(self, "スクリーン 　　:  12.4インチ")
        self.text3 = NormalText(self, "解像度 　　　　:  1536×1024")
        self.text4 = NormalText(self, "メモリ　　 　　:  4GB")
        self.text5 = NormalText(self, "ストレージ 　　:  リーズナブル ドライブ(SSD)")
        self.text6 = NormalText(self, "ソフトウェア 　:  Windows11 Home")
        self.text7 = NormalText(self, "プロセッサ　 　:  クアッドコア第11世代インテルCore")
        self.text8 = NormalText(self, "バッテリー　 　:  通常デバイス使用で最大13.5時間")
        self.set_margin(0, 6)
        self.parent.add_element(self)


class subTitle(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(19)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        # self.border("black", 2)
        # self.center_text()
        self.parent.add_element(self)


class setumeibox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(240)
        self.set_background_color("#F3F3F3")
        self.title = subTitle(self, "詳細")
        self.setumeitext = setumei(self)
        self.set_margin(24, 15)
        self.parent.add_element(self)


class textbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(70)
        self.set_background_color("#F3F3F3")
        self.rentaru = rentarutext(self, "レンタル可能")
        self.daisu = daisu(self)
        self.number = number(self.daisu, "  3")
        self.parent.add_element(self)


class CustomBox1(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(280)
        self.set_fixed_height(2)
        self.set_background_color("#F3F3F3")
        self.border_up("black", 1)
        self.set_margin(24, 0)
        self.parent.add_element(self)


class CustomBox2(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(220)
        self.set_fixed_height(2)
        self.set_background_color("#F3F3F3")
        self.border_up("black", 1)
        self.set_margin(24, 0)
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.PCname = PCtitle(self)
        self.image = imagebox(self, "res/pcbig1.png")
        self.text1 = textbox1(self)
        self.sen1 = CustomBox1(self)
        self.text2 = setumeibox(self)
        self.sen = CustomBox2(self)
        self.text3 = calendarTitle(self)

        self.parent.add_element(self)


class calendarTitle(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(22)
        self.set_text_color("black")
        self.set_text("レンタル期間選択")
        # self.border("black", 2)
        self.set_color_as_parent()
        self.set_margin(0, 10)
        self.center_text()
        self.parent.add_element(self)


class PCItem:
    def __init__(self, name, maker, uid) -> None:
        self.name = name
        self.maker = maker
        self.uid = uid


class ItemDescriptorScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.goback = GoBackButton(self.title, "<", "black", "white")
        self.scroll = scroll(self.container)
        self.set_background_color("#E6E6E6")
        self.container.set_as_core()
        self.container.build()
        self.core.eventsys.subscribe("ITEMSELECTED", lambda data: self.populate(data))
        self.core.eventsys.subscribe("USERLOGIN", lambda data: self.get_user_id(data))
        self.scroll.text3.set_signal(self.set_rental)
        self.pcid = None
        self.user_id = None
        self.rentalnumber = None

        self.pcitem = PCItem(None, None, None)

    def get_user_id(self, data):
        self.user_id = data

    def set_rental(self):
        user = self.user_id
        pcid = self.pcid
        rental_number = self.rentalnumber
        self.core.eventsys.emit(
            "DATATRANSFER", [user, pcid, rental_number, self.pcitem]
        )
        self.manager.go_to(SceneTitles.SceneRentalItemSelected)

    def populate(self, data):
        self.pcid = data[0]
        self.scroll.image.image.set_image(data[1])
        self.scroll.PCname.pcname1.set_text(data[2])
        self.scroll.PCname.pcname2.set_text(data[3])
        print(data)
        self.pcitem.uid = data[0]
        self.pcitem.maker = data[2]
        self.pcitem.name = data[3]

        remaning = requests.request("GET", f"http://renteckdb.site/pcinfo/{data[0]}")
        jsoninfo = json.loads(remaning.content)
        daisu = jsoninfo["remaining"]
        self.rentalnumber = daisu
        self.scroll.text1.number.text = f"{daisu}"
        self.scroll.text1.number.make_text_surface()
        if daisu == 0:
            self.scroll.text1.rentaru.text = "在庫切れ"
            self.scroll.text1.rentaru.make_text_surface()
            self.scroll.text3.set_signal(lambda: None)
            self.scroll.text3.text = "レンタル不可能"
            self.scroll.text3.text_color = "red"
            self.scroll.text3.make_text_surface()
        else:
            self.scroll.text1.rentaru.text = "レンタル可能"
            self.scroll.text1.rentaru.make_text_surface()
            self.scroll.text3.set_signal(lambda: None)
            self.scroll.text3.text = "レンタル期間選択"
            self.scroll.text3.text_color = "black"
            self.scroll.text3.make_text_surface()
            self.scroll.text3.set_signal(self.set_rental)
        self.scroll.image.image.resize_match_parent_width()
