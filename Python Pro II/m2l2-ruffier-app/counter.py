from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class Seconds(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        sec_text = f'Segundos transcurridos: {self.current}'
        super().__init__(text=sec_text, **kwargs)

    def start(self):
        Clock.schedule_interval(self.counter, 1)

    def restart(self, total, *args):
        self.total = total
        self.current = 0
        self.done = False
        sec_text = f'Segundos transcurridos: {self.current}'
        self.start()

    def counter(self, dt):
        self.current += 1
        self.text = f'Segundos transcurridos {self.current}'
        if self.current >= self.total:
            self.done = True
            return False


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        contador = Seconds(total=10)
        boton = Button(text='Iniciar')
        boton.on_press = contador.start

        layout.add_widget(contador)
        layout.add_widget(boton)

        return layout

if __name__ == "__main__":
    MyApp().run()



