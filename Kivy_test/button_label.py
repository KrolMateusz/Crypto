from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_y: None
    height: sp(150)
    Label: 
        text: 'Hello'
    Button:
        text: 'World'
'''))
