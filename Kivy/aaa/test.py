from kivy.app import App
from kivy.uix.textinput import TextInput


class CapitalInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        return super(CapitalInput, self).insert_text(s, from_undo=from_undo)


class MyApp(App):
    def build(self):
        return TextInput(text='Enter cipher', multiline=True)


if __name__ == '__main__':
    MyApp().run()
