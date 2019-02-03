from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
GridLayout:
    CheckBox:
        size_hint_y: None
        height: '500dp'
        active: True
'''))
