from kivy.lang.builder import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    spacing: 30
    padding: 50
    Button:
        text: 'b1'
    Button:
        text: 'b2'
'''))
