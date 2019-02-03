from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
FloatLayout:
    Scatter:
        size: 100, 100
        pos: 450, 450
        do_rotation: True
        Label:
            text: 'Something'
'''))
