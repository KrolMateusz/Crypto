from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse , Line
from random import random
from kivy.uix.button import Button

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(), random(), random())
		with self.canvas:
			Color(*color)
			t = 60
			Ellipse(pos=(touch.x - t/2, touch.y - t/2), size=(t,t))
			touch.ud['Line'] = Line(points=(touch.x, touch.y))
	def on_touch_move(self, touch):
		touch.ud['Line'].points +=[touch.x, touch.y]



class MyPintApp(App):
	def build(self):
		p = Widget()

		p2 = MyPaintWidget()
		clearbtn = Button(text='Clear')

		p.add_widget(p2)
		p.add_widget(clearbtn)

		def clear_canvas(obj):
			p2.canvas.clear()
		clearbtn.bind(on_release=clear_canvas)


		return p
		



if __name__ == '__main__':
    MyPintApp().run()
