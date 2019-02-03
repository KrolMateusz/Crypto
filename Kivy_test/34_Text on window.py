from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
	Label:
		canvas.before:
			Color:
				rgba:1,0,0,0.22
			Rectangle:
				pos:self.pos
				size:self.size
		text:'Top'
		size_hint_y:None
		hieght:sp(65)
		font_size:sp(50)

	Label:
		canvas.before:
			Color:
				rgb:1,0,0
			Rectangle:
				pos:self.pos
				size:self.size
		text:'Center'
		size_hint_y:None
		hieght:sp(65)
		size_hint_x:None
		width:sp(65)

	Label:
		canvas.before:
			Color:
				rgba:2,1,1,0.35
			Rectangle:
				pos:self.pos
				size:self.size
		text:'Botton'
		size_hint_y:None
		hieght:sp(35)


'''))
