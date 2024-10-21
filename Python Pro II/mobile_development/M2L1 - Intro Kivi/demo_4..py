from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def test():
    print('CLICK!!')

class MyApp(App):
    def build(self):
        text = Label(text='Soy un texto, leeme', color=(1, 0.6, 1, 1), font_size=30)
        btn = Button(text='Boton -> CLICK', color=(1, 0.6, 0.2, 1), font_size=50)
        btn.on_press = test
        # el método on_press del objeto btn se vuelve igual a la función test
        # es decir, llamar a btn.on_press() es equivalente a llamar test()
        # un método nombrado on_press es llamado automáticamente cuando se hace clic en el botón

        layout = BoxLayout(orientation='vertical', padding=20, spacing=50)
        layout.add_widget(btn)
        layout.add_widget(text)

        return layout

app = MyApp()
app.run()


