from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
# ScreenManager es un widget especial que hace visible una de las pantallas especificadas en él.


class MainScreen(Screen):
    # screen es un widget en el cual todos los otros (descendientes) pueden ser creados
    def __init__(self, name='first'):
        super().__init__(name=name) # el nombre de la pantalla debe ser pasado al constructor de la clase Screen
        btn = Button(text = 'Cambiar a otra pantalla', font_size=30, color=(1, 0.6, 0.2, 1))
        self.add_widget(btn)
        btn.on_press = self.next_screen

    def next_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text='Regresar a la Pantalla principal', font_size=30, color=(222, 28, 22, 0.8))
        self.add_widget(btn)
        btn.on_press = self.prev_screen

    def prev_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen())
        screen_manager.add_widget(SecondScreen())
        # MainScreen se inicalizá porque fue añadido primero.
        return screen_manager


app = MyApp()
app.run()
