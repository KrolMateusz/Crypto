from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
Label:
    Button:
        text: 'Mathew'
        font_size: 32
        color: 0.8, 0.9, 0, 1
        size: 200, 100
        pos: 50, 100
    Button:
        text: 'Another Mathew'
        font_size: 20
        color: 0.8, 0.9, 1, 1
        size: 200, 100
        pos: 50, 200
'''))
