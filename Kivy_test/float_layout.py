from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
<Button>:
    color: 0.8, 0.2, 0, 1
    font_size: 50
    size_hint: 0.3, 0.2

FloatLayout:
    Button:
        text: 'B1'
        pos_hint: {'x': 0, 'top': 1}
    Button:
        text: 'B2'
        pos_hint: {'y': 0, 'right': 1}
'''))
