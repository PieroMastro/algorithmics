from kivy.app import App
from kivy.uix.label import Label

# Clase que hereda de la clase App toda la funcionalidad
class MyApp(App):
    def build(self):
        # Agregando un widget
        text = Label(text='Soy Texto', font_size=50, color=(1, 0.988, 0.216))
        return text

app = MyApp()
app.run()


