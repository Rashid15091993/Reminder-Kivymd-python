from kivymd.uix.button import MDIconButton,MDRoundFlatButton
from kivy.lang import Builder
from kivy.animation import Animation 
from kivy.core.window import Window 
class ListButton(MDRoundFlatButton):
    Builder.load_file('list_button.kv')
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__revealed = None
        self.__open = None
        self.__moved = None

    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            if self.__open:
                return False

            touch.grab(self)
            return True

        return False

    def on_touch_move(self,touch):
         if self.collide_point(touch.x,touch.y):
            if self.__moved:
                return False

            if self.__open:
                self.__open = None

            else:
                self.__open = True

            self.reveal()
            self.__moved = True

    def on_touch_up(self,touch):
        if self.collide_point(touch.x,touch.y):
            touch.ungrab(self)
            self.__moved = None

            return True
        return False

    def reveal(self):
        if self.__revealed:
            pos = 20

            anim = Animation(x = pos,duration = 0.1)
            anim.start(self)
            self.__revealed = False
        else:
            pos = -Window.width / 8

            anim = Animation(x = pos,duration = 0.1)
            anim.start(self)
            self.__revealed = True