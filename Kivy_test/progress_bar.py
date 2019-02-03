from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
BoxLayout:
    padding: 100
    ProgressBar:
        id: bar
        max: 100
        value: 90
'''))
