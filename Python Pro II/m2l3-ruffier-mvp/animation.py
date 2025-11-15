from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.core.window import Window

class AnimatedBtn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.start_color = list(self.background_color)
        self.start_position = self.pos_hint

        self.anime_forward = (
            Animation(background_color=(0.9, 0.2, 0.1, 1), duration=1) +
            Animation(pos_hint={'center_x': 0.5, 'y': 0.8}, duration=1) 
        )

        self.anime_back = Animation(
            background_color=self.start_color, 
            pos_hint=self.start_position, 
            duration=1
        )

        self.anime = self.anime_forward + self.anime_back

    def start_animation(self):
        Animation.cancel_all(self)
        self.anime.start(self)


class MyApp(App):
    def build(self):
        # Usamos FloatLayout para que las animaciones de 'pos_hint' funcionen.
        container = FloatLayout()
        
        text = Label(
            text='Click en el botón para animarlo!', 
            size_hint=(1, 0.2), 
            pos_hint={'top': 1} 
        )
        container.add_widget(text)
        
        btn = AnimatedBtn(
            text='Click!', 
            background_color=(0, 0.6, 0.9, 1),
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.0} 
        )
        btn.on_press = btn.start_animation

        container.add_widget(btn)
        return container

app = MyApp()
app.run()
