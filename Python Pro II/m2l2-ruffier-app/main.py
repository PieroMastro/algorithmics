from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Contenido de las instrucciones
from instructions import instructions_text, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import ruffier_index

# Variables Globales
age = 7
name = ''
pulse_1, pulse_2, pulse_3 = 0, 0, 0

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

        inst_text = Label(text=txt_test1, halign='center', valign='top')
        pulse1_text = Label(text='Ingresar el pulso:', halign='left', size_hint_x=0.5)
        self.pulse1_input = TextInput(multiline=False, size_hint_x=1.0)
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        line_1 = BoxLayout(size_hint_y=None, height='30sp')
        line_1.add_widget(pulse1_text)
        line_1.add_widget(self.pulse1_input)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(line_1)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_1
        pulse_1 = int(self.pulse1_input.text)
        self.manager.current = 'sits'


class SitsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        inst_text = Label(text=txt_test2, halign='center', valign='top')
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        self.manager.current = 'pulse2'


class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        inst_text = Label(text=txt_test3, halign='center', valign='top')
        pulse2_text = Label(text='Resultado:', halign='left', size_hint_x=0.5)
        self.pulse2_input = TextInput(multiline=False, size_hint_x=1.0)
        pulse3_text = Label(text='Resultado despues del descanso:', halign='left', size_hint_x=0.5)
        self.pulse3_input = TextInput(multiline=False, size_hint_x=1.0)
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        line_1 = BoxLayout(size_hint_y=None, height='30sp')
        line_1.add_widget(pulse2_text)
        line_1.add_widget(self.pulse2_input)

        line_2 = BoxLayout(size_hint_y=None, height='30sp')
        line_2.add_widget(pulse3_text)
        line_2.add_widget(self.pulse3_input)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(line_1)
        main_layout.add_widget(line_2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_2, pulse_3
        pulse_2 = int(self.pulse2_input.text)
        pulse_3 = int(self.pulse3_input.text)
        self.manager.current = 'result'


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.indice = Label(text='Tu índice de Ruffier es: ', halign='left', valign='top')
        self.resultado = Label(text='Aqui va el resultado: ', halign='left', valign='top')
        self.button = Button(text='Volver al Inicio', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(self.indice)
        layout.add_widget(self.resultado)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def next(self):
        self.manager.current = 'main'
        self.manager.transition.direction = 'left'

    def on_enter(self, *args):
        global name
        self.indice.text = str(ruffier_index(pulse_1, pulse_2, pulse_3))
        self.indice.text = f'{name}, ¡Tu índice de Ruffier es: {self.indice.text}!'

class RuffierApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name='main'))
        manager.add_widget(Pulse1Screen(name='pulse1'))
        manager.add_widget(SitsScreen(name='sits'))
        manager.add_widget(Pulse2Screen(name='pulse2'))
        manager.add_widget(ResultScreen(name='result'))

        return manager

app = RuffierApp()

if __name__ == "__main__":
    app.run()
