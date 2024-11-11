from kivy.uix.label import Label
from kivy.clock import Clock as clock
from kivy.properties import BooleanProperty

class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        my_text = f"Segundos transcurridos: {self.current}"
        super().__init__(text=my_text)

    def start(self):
        clock.schedule_interval(self.update, 1)
        
    def update(self, dt):
        self.current += 1
        self.text = f"Segundos transcurridos: {self.current}"
        if self.current >= self.total:
            self.done = True
            return False

    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = f"Segundos transcurridos: {self.current}"
        self.start()
