from kivy.base import runTouchApp
from kivy.base import Builder

runTouchApp(Builder.load_string('''
PageLayout:
    Button:
        text: 'B1'
    Button:
        text: 'B1'
    Button:
        text: 'B1'
'''))
