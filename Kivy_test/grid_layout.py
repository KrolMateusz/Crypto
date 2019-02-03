from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
GridLayout:
    rows: 1
    spacing: 10
    padding: 100
    size_hint_x: None
    Button:
        text: 'B1'
        size_hint_x: None
        width: 200
    Button:
        text: 'B2'
        size_hint_x: None
        width: 200
'''))
