from kivy.uix.label import Label
from kivy.app import App


class Controller2App(App):
    def build(self):
        return Label(text='[color=ff3333][sub]Hello[/sub][/color]'
                          '[color=3333ff][b]World[/b][/color]',
                     markup=True, font_size=50)


if __name__ == '__main__':
    Controller2App().run()
