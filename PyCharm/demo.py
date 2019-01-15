import kivy
kivy.require('1.6.0')

from kivy.app import App
from kivy.uix.label import Label

class MyDemoApp(App):
    def build(self):
        return Label(text = "bu demo ekranıdır")

if __name__ == "__main__":
    MyDemoApp().run()