from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
GridLayout:
    canvas:
        Color: 
            rgb: 1, 2, 0
        Rectangle:
            pos: self.pos
            size: self.size
'''))
