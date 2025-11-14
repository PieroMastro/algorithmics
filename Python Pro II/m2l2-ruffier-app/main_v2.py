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
from seconds import Seconds

# Variables Globales
age = 7
name = ''
pulse_1, pulse_2, pulse_3 = 0, 0, 0

# Manejo de excepciones
def check_int(number:str):
    try:
        return int(number)
    except ValueError:
        return False

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
        age = check_int(self.age_input.text)
        if age == False or age < 7:
            age = 7
            self.age_input.text = str(age)
        else:
            self.manager.current = 'pulse1'


class Pulse1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        inst_text = Label(text=txt_test1, halign='center', valign='top')
        pulse1_text = Label(text='Ingresar el pulso:', halign='left', size_hint_x=0.5)
        self.pulse1_input = TextInput(multiline=False, size_hint_x=1.0)
        # Inhabilitar el campo de ingreso de data
        self.pulse1_input.set_disabled(True)
        self.button = Button(text='Siguiente', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next
        # 🟢 Inicialización de la clase Seconds con el nuevo constructor
        self.timer = Seconds(total=5)
        self.timer.bind(done=self.timer_finished)

        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        line_1 = BoxLayout(size_hint_y=None, height='30sp')
        line_1.add_widget(pulse1_text)
        line_1.add_widget(self.pulse1_input)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(line_1)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def timer_finished(self, *args):
        self.pulse1_input.set_disabled(False)
        self.button.set_disabled(False)
        self.button.text = "Continuar"
        self.next_screen = True

    def next(self):
        global pulse_1

        if not self.next_screen:
            self.button.set_disabled(True)
            self.timer.start()
        else:
            pulse_1 = check_int(self.pulse1_input.text)
            
            if pulse_1 is False or pulse_1 < 8:
                pulse_1 = 0
                self.pulse1_input.text = str(pulse_1)
            else:
                self.manager.current = 'sits'


class SitsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        self.timer = Seconds(total=5)
        self.timer.bind(done=self.sec_finished)
        inst_text = Label(text=txt_test2, halign='center', valign='top')
        self.button = Button(text='Iniciar', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def sec_finished(self, *args):
        self.button.set_disabled(False)
        self.button.text = 'Continuar'
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.button.set_disabled(True)
            self.timer.start()
        else:
            self.manager.current = 'pulse2'


class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Estado 0: Iniciar P2 | 1: Ingreso P2 + Iniciar Descanso | 2: Descanso Terminado + Iniciar P3 | 3: Ingreso P3 + Validar
        self.stage = 0 
        
        inst_text = Label(text=txt_test3, halign='center', valign='top', size_hint_y=0.2)
        self.status_label = Label(text='Pulsa "Iniciar P2" para iniciar la medición', size_hint_y=0.1)

        # 🟢 Inicialización de la clase Seconds con el nuevo constructor (usamos 15s como valor inicial)
        self.timer = Seconds(total=15)
        self.timer.bind(done=self.timer_finished)

        # Campos de Pulso
        pulse2_text = Label(text='Pulso 2 (Inmediato):', halign='left', size_hint_x=0.5)
        self.pulse2_input = TextInput(multiline=False, size_hint_x=1.0)
        pulse3_text = Label(text='Pulso 3 (Post-Descanso):', halign='left', size_hint_x=0.5)
        self.pulse3_input = TextInput(multiline=False, size_hint_x=1.0)
        
        self.pulse2_input.set_disabled(True)
        self.pulse3_input.set_disabled(True)
        
        self.button = Button(text='Iniciar P2 (15s)', size_hint=(0.3, 0.075), pos_hint={'center_x': 0.5})
        self.button.on_press = self.next

        # Layouts
        main_layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        line_status = BoxLayout(size_hint_y=0.2)
        line_status.add_widget(self.status_label)
        line_status.add_widget(self.timer)

        line_1 = BoxLayout(size_hint_y=None, height='30sp')
        line_1.add_widget(pulse2_text)
        line_1.add_widget(self.pulse2_input)

        line_2 = BoxLayout(size_hint_y=None, height='30sp')
        line_2.add_widget(pulse3_text)
        line_2.add_widget(self.pulse3_input)

        main_layout.add_widget(inst_text)
        main_layout.add_widget(line_status)
        main_layout.add_widget(line_1)
        main_layout.add_widget(line_2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def timer_finished(self, *args):
        # El temporizador ha terminado en la etapa actual
        if self.stage == 0:
            # P2 terminado. Habilitar entrada y cambiar botón a Descanso
            self.status_label.text = '¡TIEMPO! Ingresa el Pulso 2 y pulsa "Descanso"'
            self.button.text = 'Descanso (30s)'
            self.button.set_disabled(False)
            self.pulse2_input.set_disabled(False)
            self.stage = 1
            
        elif self.stage == 1:
            # Descanso terminado. Iniciar P3
            self.status_label.text = '¡TIEMPO! Pulsa "Start P3" para la medición final'
            self.button.text = 'Iniciar P3 (15s)'
            self.button.set_disabled(False)
            self.stage = 2
            
        elif self.stage == 2:
            # P3 terminado. Habilitar entrada y cambiar botón a Finalizar
            self.status_label.text = '¡FINALIZADO! Ingresa el Pulso 3 y pulsa "Finalizar"'
            self.button.text = 'Finalizar'
            self.button.set_disabled(False)
            self.pulse3_input.set_disabled(False)
            self.stage = 3 # Listo para validar

    def next(self):
        if self.stage == 0:
            # Etapa 0: Iniciar P2 (15s)
            self.button.set_disabled(True)
            self.status_label.text = 'Contando 15 segundos para Pulso 2...'
            self.timer.restart(15)

        elif self.stage == 1:
            # Etapa 1: Tomar P2 e Iniciar Descanso (30s)
            global pulse_2
            pulse_2 = check_int(self.pulse2_input.text)
            
            if pulse_2 == False or pulse_2 < 8:
                pulse_2 = 0
                self.pulse2_input.text = str(pulse_2)
                self.status_label.text = 'Error en Pulso 2. Debe ser > 0 y numérico.'
                return
            
            # 2. Iniciar descanso
            self.pulse2_input.set_disabled(True)
            self.button.set_disabled(True)
            self.status_label.text = 'Descanso de 30 segundos...'
            self.timer.restart(30)
            
        elif self.stage == 2:
            # Etapa 2: Iniciar P3 (15s)
            self.button.set_disabled(True)
            self.status_label.text = 'Contando 15 segundos para Pulso 3...'
            self.timer.restart(15)
            
        elif self.stage == 3:
            # Etapa 3: Validar P3 y Avanzar
            global pulse_3
            pulse_3 = check_int(self.pulse3_input.text)
            
            if pulse_3 == False or pulse_3 < 8:
                pulse_3 = 0
                self.pulse3_input.text = str(pulse_3)
                self.status_label.text = 'Error en Pulso 3. Debe ser > 0 y numérico.'
            else:
                self.manager.current = 'result'


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.indice = Label(text='Tu índice de Ruffier es: ', halign='left', valign='top')
        self.resultado = Label(text='CORRELACIONAR INDICE Y RESULTADO', halign='left', valign='top')
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
