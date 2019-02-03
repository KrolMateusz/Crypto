from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
	orientation:'vertical'
	padding: 50
	Slider:
		max:450
		value:20
		id:Sl

	ProgressBar:
		max:450
		value:Sl.value

	Slider:
		max:600
		on_value:Sl.value = self.value

'''))
