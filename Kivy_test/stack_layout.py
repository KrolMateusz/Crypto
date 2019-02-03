from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
StackLayout:
    orientation: 'rl-tb'
    padding: 20
    spacing: 10
    Button:
        text: 'Button'
        size_hint: 0.2, 0.1
    Button:
        text: 'Button'
        size_hint: 0.2, 0.1
    Button:
        text: 'Button'
        size_hint: 0.2, 0.1
    Button:
        text: 'Button'
        size_hint: 0.2, 0.1
        
'''))
