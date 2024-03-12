import kivy
from kivy.app import App
from kivy.uix.label import Label

# This line is optional but will suppress Kivy's default logging output
kivy.config.Config.set('kivy', 'log_level', 'error')

class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello, World!')

if __name__ == '__main__':
    HelloWorldApp().run()
