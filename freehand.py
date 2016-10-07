from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import *
import os.path

class FreeHandWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 20.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width = 5, cap = "round", joint = "round")

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class FreeHandApp(App):

    def build(self):
        parent = Widget()
        self.painter = FreeHandWidget()
        clearbtn = Button(text='New')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    FreeHandApp().run()
