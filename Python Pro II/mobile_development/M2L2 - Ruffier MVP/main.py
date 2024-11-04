from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=5, spacing=10)
        instructions = Label(text=txt_instruction, font_size= 18)
        
        
        layout.add_widget(instructions)
        self.add_widget(layout)







class RuffierTest(App):
    def build(self):
        scr_manager = ScreenManager()
        scr_manager.add_widget(MainScreen(name='main'))

        return scr_manager

app = RuffierTest()
app.run()