from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import ruffier_index

# VARIABLES GLOBALES
name = ''
age = 7
pulse_1, pulse_2, pulse_3 = 0, 0, 0

class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Widgets que conforman la pantalla
        instructions = Label(text=txt_instruction)
        name_text = Label(text='Ingrese su nombre:', halign='right')
        self.name_input = TextInput(multiline=False)
        age_text = Label(text='Ingrese su edad:', halign='right')
        self.age_input = TextInput(text='7', multiline=False)
        self.button = Button(text='Inicio', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        # 2 Layouts horizontales, texto / input
        input_line_1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        input_line_2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        input_line_1.add_widget(name_text)
        input_line_1.add_widget(self.name_input)
        input_line_2.add_widget(age_text)
        input_line_2.add_widget(self.age_input)

        # Configuracion del layout primario
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(instructions)
        main_layout.add_widget(input_line_1)
        main_layout.add_widget(input_line_2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
            global name
            name = self.name_input.text
            self.manager.current = 'pulse1'


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instructions = Label(text=txt_test1)
        input_line = BoxLayout(size_hint=(0.8, None), height='30sp')
        pulse_1_text = Label(text='Ingresar el resultado:', halign='right')
        self.pulse_1_input = TextInput(text='0', multiline=False)
        
        input_line.add_widget(pulse_1_text)
        input_line.add_widget(self.pulse_1_input)
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(instructions)
        main_layout.add_widget(input_line)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_1
        pulse_1 = int(self.pulse_1_input.text)
        self.manager.current = 'sits'


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instructions = Label(text=txt_sits)
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(instructions)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        # WIDGETS
        super().__init__(**kwargs)
        instructions = Label(text=txt_test3)
        pulse_2_text = Label(text='Resultado:', halign='right')
        self.pulse_2_input = TextInput(text='0', multiline=False)
        pulse_3_text = Label(text='Resultado después de descanso:', halign='right')
        self.pulse_3_input = TextInput(text='0', multiline=False)
        self.button = Button(text='Finalizar', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        # LAYOUT
        input_line_1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        input_line_1.add_widget(pulse_2_text)
        input_line_1.add_widget(self.pulse_2_input)
        input_line_2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        input_line_2.add_widget(pulse_3_text)
        input_line_2.add_widget(self.pulse_3_input)

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(instructions)
        main_layout.add_widget(input_line_1)
        main_layout.add_widget(input_line_2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_2, pulse_3
        pulse_2 = int(self.pulse_2_input.text)
        pulse_3 = int(self.pulse_3_input.text)
        self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.results = Label(text='')
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.main_layout.add_widget(self.results)
        self.add_widget(self.main_layout)
        self.on_enter = self.get_results

    def get_results(self):
        global name
        self.results.text = f"{name}\nIndice de Ruffier: {ruffier_index(pulse_1, pulse_2, pulse_3)}"



class RuffierApp(App):
    def build(self):
        scr_manager = ScreenManager()
        scr_manager.add_widget(IntroScreen(name='main'))
        scr_manager.add_widget(PulseScr(name='pulse1'))
        scr_manager.add_widget(CheckSits(name='sits'))
        scr_manager.add_widget(PulseScr2(name='pulse2'))
        scr_manager.add_widget(Result(name='result'))

        return scr_manager

app = RuffierApp()
app.run()