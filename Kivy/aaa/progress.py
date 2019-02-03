from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

x = ['a', 'b', 'c', 'd', 'e']
y = [6, 7, 8, 2, 4]

plt.bar(x,y, label='Bars1', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck It out')
plt.legend()


class Patient(Screen):
    pass


class Progress(Screen):
    bar = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.bar.clear_widgets()
        self.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class Manager(ScreenManager):
    pass


class ProgressApp(App):
    title = "Kivy Garden Matplolib & plt"

    def build(self):
        return Manager()


if __name__ == "__main__":
    ProgressApp().run()