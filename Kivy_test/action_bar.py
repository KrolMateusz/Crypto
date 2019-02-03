from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint: {'top': 1}
    
    ActionView:
        ActionPrevious:
            title: 'Action Bar'
            with_previous: False
        ActionButton:
            text: 'Button'
            icon: 'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            text: 'Button'
        ActionButton:
            text: 'Button'
        ActionButton:
            text: 'Button'
        ActionGroup:
            text: 'Group'
            color: 0.3, 0.9, 0, 1
            font_size: 15
            ActionButton:
                text: 'Button'
            ActionButton:
                text: 'Button'
            ActionButton:
                text: 'Button'
            ActionButton:
                text: 'Button'
            ActionButton:
                text: 'Button'
'''))
