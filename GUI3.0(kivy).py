from kivy.app import App

from kivy.uix.button import Button

class TestApp(App):
    def build(selfself):
        return Button(text='User Login')

TestApp().run()
