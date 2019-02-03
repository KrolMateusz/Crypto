from kivy.app import App
from kivy.lang import Builder

kv = """
BoxLayout:
	orientation: 'vertical'
	CheckBox:
		group:'a'
		active: True

	CheckBox:
		id: Ch
		group:'a'


	Button:
		text:'Yes'
		on_press: Ch.active = True
	Button:
		text:'No'
		on_press: Ch.active = False



"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
