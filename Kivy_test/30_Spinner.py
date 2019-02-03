from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp

s = Spinner(
	text='Home',
	values=('Home', 'Work', 'Costom', 'Other'),

	size_hint=(None, None),
	size=(100,44),
	pos_hint={'center_x':.5, 'center_y':.5}

	)
def Show_value(spinner, text):
	print('the spinner have text', text)

s.bind(text=Show_value)


runTouchApp(s)
