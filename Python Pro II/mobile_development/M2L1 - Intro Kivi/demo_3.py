from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        # al crear un widget, se puede establecer los valores de sus propiedades
        # ¡los constructores de widget solo aceptan parámetros con nombre!
        btn = Button(text='Boton -> CLICK', color=(1, 0.6, 0.2, 1), font_size=50)
        text = Label(text='Soy un texto, leeme', color=(1, 0.6, 1, 1), font_size=30)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=50)
        layout.add_widget(btn)
        layout.add_widget(text)

        return layout # retorna un widget que controla el diseño de sus hijos

app = MyApp()
app.run()


