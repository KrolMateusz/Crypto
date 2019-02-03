from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App


class Controller2(FloatLayout):
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)

        button = Button(text='Hello World', font_size=10, color=(.9, .8, 0, 1),
                        pos_hint={'x': 0.7, 'y': 0.8}, size_hint=(0.1, 0.1))
        self.add_widget(button)


class Controller2App(App):
    def build(self):
        return Controller2()


if __name__ == '__main__':
    Controller2App().run()
