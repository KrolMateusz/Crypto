from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
RelativeLayout:
    Button:
        text: 'B1'
        size_hint: 0.4, 0.4
        pos: 10, 70
    Button:
        text: 'B2'
        size_hint: 0.2, 0.1
        pos_hint: {'x': 0.4, 'y': 0.5}
'''))
