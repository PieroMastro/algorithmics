# programa con tres pantallas, el cambio a la tercera pantalla se produce por temporizador
# el temporizador se habilita en el método on_enter de la segunda pantalla, es decir, inmediatamente después de que el usuario ha entrado en esta pantalla
# ver línea 58

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

time_to_read = 5
long_txt = """Utilice estos consejos para aumentar su velocidad de lectura:\n
1. No pronuncie el texto legible.\n
Si ya tiene el hábito de pronunciar, practique la lectura y simultáneamente cante una nota con los labios cerrados.\n 
2. Aprenda a comprender varias palabras a la vez.\n
Practica echando un vistazo al texto. Sin mover la mirada, cierre los ojos y recuerde lo que ha leído.\n 
3. Mueva su mirada de arriba hacia abajo.\n
No mires atrás a lo que ya has leído. Practica leer columnas de texto estrechas.\n
Puede ayudarse moviendo una hoja de papel sobre el texto para que cubra la parte superior de la página. Acelera el movimiento de la hoja.\n
4. Concéntrate en la lectura.\n
Leer textos largos. Elimina las distracciones. Busque libros que le cautiven. """

# clase para mostrar prolijamente texto largo en una pequeña pantalla de desplazamiento
# puedes leer más en la documentación de la primera lección
class ScrollLabel(ScrollView):
    def __init__(self, ltext, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text=ltext, markup=True, size_hint_y=None, font_size='20sp', halign='left', valign='top')
        self.label.bind(size=self.resize)
        self.add_widget(self.label)

    def resize(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=10)
        box.add_widget(Label(text="Intenta leer el texto en " + str(time_to_read) + " segundo(s)"))
        btn_next = Button(text="Comienzo", on_press=self.next)
        box.add_widget(btn_next)
        self.add_widget(box) 

    def next(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = 'showtext' 

class ShowText(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(padding=10)
        box.add_widget(ScrollLabel(long_txt, size_hint_x=0.8, pos_hint={'center_x':0.5})) 
        self.add_widget(box)
    
    def on_enter(self):
        Clock.schedule_once(self.next, time_to_read)

    def next(self, dt):
        print(dt, " pasaron los segundos ")
        self.manager.current = 'last' 

class LastScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Tiempo!")) 

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='1'))
        sm.add_widget(ShowText(name='showtext'))
        sm.add_widget(LastScr(name='last'))
        return sm

app = MyApp()
app.run()