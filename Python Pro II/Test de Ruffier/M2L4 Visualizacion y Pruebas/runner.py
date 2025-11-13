from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    value = NumericProperty(0) # Contador actual de sentadillas
    finished = BooleanProperty(False) # Estado para finalizar

    def __init__(self, total=10, steptime=1, bg_color=(1, 0.9, 0, 1), txt_progress='Sentadilla', **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.txt_progress = txt_progress

        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime / 2) + Animation(pos_hint={'top': 1}, duration=steptime / 2))
        
        # Usar on_complete para conteo en repeticiones
        self.animation.repeat = True
        self.animation.bind(on_complete=self.next) 

        self.btn = Button(
            pos_hint={'top': 1},
            size_hint=(1, 0.1),
            background_color=bg_color,
            text=txt_progress
        )
        self.add_widget(self.btn)

    def restart(self, total):
        self.total = total
        self.start()

    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True       
        # Iniciar la animación SIEMPRE
        self.animation.start(self.btn)

    def next(self, animation, widget): 
        self.value += 1

        if self.value >= self.total:
            self.animation.stop(self.btn)
            self.btn.text = f"¡{self.total} Completadas!"
            self.finished = True
