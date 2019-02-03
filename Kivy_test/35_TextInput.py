
from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
	TextInput:
		size_hint:None, None
		size: 400, 100
		text:'Select this text'
		use_bubble:True
		use_handles:True
		password:False
		readonly:False


"""


class Test1(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    Test1().run()
