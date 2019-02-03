from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<BoxLayout>:
    orientation: 'vertical'
    Button:
        text:'B1'
    Button:
        text:'B2'
    Button:
        text:'B3'
''')


class MyList(BoxLayout):
    pass


if __name__ == '__main__':
    runTouchApp(MyList())
