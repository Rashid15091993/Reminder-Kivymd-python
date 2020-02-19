from kivymd.app import MDApp
from kivy.lang import Builder
import os
from kivymd.uix.button import MDIconButton,MDRoundFlatButton
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.theming import ThemableBehavior
from kivy.properties import ObjectProperty,ListProperty,OptionProperty
from data_base import DataBase
import sqlite3 as sql
from kivy.metrics import dp
from kivymd.color_definitions import colors, palette
from kivy.uix.floatlayout import FloatLayout
from listbutton import ListButton

class ButtonMDIcon(IRightBodyTouch,  MDIconButton):
    pass

class ListScreen(Screen,BoxLayout):
    pass
        
class MyScreenManager(ScreenManager):
    sm = ObjectProperty()#ScreenManager
    box = ObjectProperty()#list Object Screen:'screen_menu'
    text_list = ObjectProperty() #input a Screen:'add_list1' text list

    # my lists widget input function
    def add_list(self):
        con = sql.connect('base.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS 'base'('list1' BINARY 'list2' BINARY)")
            list1 = self.text_list.text
            cur.execute(f"INSERT INTO 'base' VALUES('{list1}')")
            con.commit()
            cur.close()

        btn = ListButton(text = str(list1))
        btn.md_bg_color = 1, 1, 1, .5  
        btn.size_hint_x = .5                                 
        self.box.add_widget(btn)

class ColorSelector(MDIconButton):
    color_name = OptionProperty("Indigo", options=palette)
    
class Reminder(MDApp,DataBase):

    def build(self):
        self.base_list()
        self.main = Builder.load_file('main.kv')

        return self.main

    def on_start(self):

        con = sql.connect('base.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM 'base'")
        rows = cur.fetchall()

        for row in rows:
            btn = ListButton(text = str(row[0]))
            btn.size_hint_x = .5
            btn.md_bg_color = 1, 1, 1, .5                                
            self.root.ids.box.add_widget(btn)

    def on_clear(self):  # Будет вызвана в момент закрытия экрана

        self.root.ids.box.clear_widgets()

if __name__ == '__main__':
    Reminder().run()
