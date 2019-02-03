from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

class CarouselApp(App):
	def build(self):
		c = Carousel(direction='left', loop = True)
		for i in range(10):
			src = "http://placehold.it/480x270.png& text=Slide- %d" %i
			image = AsyncImage(source = src)
			c.add_widget(image)
		return c






CarouselApp().run()