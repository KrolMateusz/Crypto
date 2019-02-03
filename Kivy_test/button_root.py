from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''
Label:
    Button:
        text: 'Hello'
        pos: root.x, root.top - self.height
    Button:
        text: 'World'
        pos: root.right - self.width, root.y
'''))
