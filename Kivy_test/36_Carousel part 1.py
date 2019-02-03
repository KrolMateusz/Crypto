from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.carousel import Carousel

Builder.load_string("""

<MyWidget>:
	direction:'left'
	loop: True
	Label:
		text:'Screen 1'
	Label:
		text:'Screen 2'
	Label:
		text:'Screen 3'
""")

class MyWidget(Carousel):
	pass

class MyApp(App):
	def build(self):
		return MyWidget()

if __name__ == '__main__':
	MyApp().run()
