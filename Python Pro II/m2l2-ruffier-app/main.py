from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Contenido de las instrucciones
from instructions import instructions_text

# Variables Globales
age = 7
name = ''
pulse_1, pulse_2, pulse_3 = 0, 0, 0

# Configuración básica de la ventana
# Window.size = (400, 500)


# Pantalla de inicio
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 1. Widgets de información
        inst_text = Label(text=instructions_text, halign='left', valign='top')
        name_text = Label(text='Ingresar el Nombre:', halign='left', size_hint_x=0.5)
        age_text = Label(text='Ingresar la edad:', halign='left', size_hint_x=0.5)
        
        # 2. Widgets de entrada de usuario (almacenados como propiedades)
        self.name_input = TextInput(multiline=False, size_hint_x=1.0)
        self.age_input = TextInput(text='7', multiline=False, input_filter='int', size_hint_x=1.0)

        # 3. Botón para avanzar
        self.button = Button(text='Iniciar', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        # Layout Principal
        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        # Fila 1: Nombre
        line_1 = BoxLayout(size_hint_y=None, height='30sp')
        line_1.add_widget(name_text)
        line_1.add_widget(self.name_input)

        # Fila 2: Edad
        line_2 = BoxLayout(size_hint_y=None, height='30sp')
        line_2.add_widget(age_text)
        line_2.add_widget(self.age_input)
        

        # Añadir todos los layouts al layout principal
        main_layout.add_widget(inst_text)
        main_layout.add_widget(line_1)
        main_layout.add_widget(line_2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)


    def next(self):
        global name, age
        name = self.name_input.text.strip()
        age = int(self.age_input.text)

        self.manager.current = 'pulse1'


class Pulse1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='Cargando datos...')
        self.button = Button(text='Volver al Inicio', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(self.label)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def next(self):
        self.manager.current = 'main'
        self.manager.transition.direction = 'left'

    def on_enter(self, *args):
        global name
        self.label.text = f'¡Bienvenid@, {name}!' 


class RuffierApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name='main'))
        manager.add_widget(Pulse1Screen(name='pulse1')) 

        return manager

app = RuffierApp()

if __name__ == "__main__":
    app.run()
