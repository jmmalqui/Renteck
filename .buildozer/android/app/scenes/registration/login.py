import ast
import json
import os

import requests
from mesa import *
import pygame as pg
from mesa.info_tag.tag import InfoTagLevels

from utils.goback_button import GoBackButton


class LoginScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#E6E6E6")
        self.container = MesaStackVertical(self)
        self.title1 = Title1(self.container, "ログイン")  # 上部ラベル
        self.title2 = RenteckTitle(self.container, "Renteck")  # RRenteck
        self.text1 = CredentialsTextPlaceholder(self.container, "ニックネーム", 30)
        self.core.info_tag.set_font("res/NotoSansJP-Regular.ttf")
        self.input1 = CredentialsInputBox(self.container)
        self.text2 = TextHolder(self.container, "パスワード", 30)
        self.input2 = MyInputBox2(self.container)
        self.MyButton2 = LoginButton(self.container, "ログイン", "white", "black")
        self.text3 = TextHolder(self.container, "アカウントをお持ちでない方", 15)
        self.MyButton3 = NewLoginRedirectButton(
            self.container, "新規会員登録", "blue", "#E6E6E6"
        )
        self.container.set_as_core()
        self.container.build()

        self.MyButton2.set_signal(self.login)

    def login(self):
        pw = self.input2.get_written_text()
        username = self.input1.get_written_text()
        if not pw:
            self.text2.set_text("パスワードが必要")
            self.text2.set_text_color("red")
        if not username:
            self.text1.set_text("ニックネームが必要")
            self.text1.set_text_color("red")

        if username != "" and pw != "":
            if self.account_exists(username, pw):
                self.core.userid = username
                self.core.eventsys.emit("USERLOGIN", self.core.userid)

                self.manager.go_to("item-list", False)
                self.core.info_tag.inform(f"おかえりなさい    {username}")
                self.core.hide_keyboard()
            else:
                self.core.info_tag.inform(
                    "入力されたアカウントかパスワードは間違ってます", InfoTagLevels.CRITICAL
                )

    def account_exists(self, u, p):
        req = requests.request("GET", f"http://renteckdb.site/login/{u}/{p}")
        decoded = json.loads(req.content)
        return decoded["valid"]


class MyApplication(MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.main_scene = LoginScene(self, "main", self.scene_manager)
        self.scene_manager.set_init_scene("main")


# ラベル（上部）
class Title1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)

        self.set_width_as_display()
        self.set_fixed_height(int(60))
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


# 戻るボタン（画面左上）
class MyButton1(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_fixed_height(60)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    # ボタンが押されたときの処理（前画面に戻る）
    def show_press(self):
        ...


# Renteck文字
class RenteckTitle(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_height(120)
        self.set_width_as_display()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(55)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


# テキスト（メールアドレス）
class CredentialsTextPlaceholder(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


# 入力テキストボックス（メールアドレス）
class CredentialsInputBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("gray", 1)
        self.center_text_vertical()
        self.parent.add_element(self)


# テキスト（パスワード）
class TextHolder(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


# 入力テキストボックス（パスワード）
class MyInputBox2(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.password()
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("gray", 1)
        self.center_text_vertical()
        self.parent.add_element(self)


# ログインボタン
class LoginButton(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(150)
        self.set_margin(100, 50)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)


# テキスト（アカウントをお持ちでない方）
class TextHolder(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#E6E6E6")
        self.center_text()
        self.parent.add_element(self)


class NewLoginRedirectButton(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(15)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        self.move_to_screen("new-reg")
