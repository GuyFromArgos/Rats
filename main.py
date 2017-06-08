from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button

sound = SoundLoader.load('squeak.wav')
music = SoundLoader.load('ratmovie.wav')
music.play()      
class BorderButtonScreen(Widget):
     def click(self):
         sound.play()

class BorderButtonApp(App):
    def build(self):
        return BorderButtonScreen()

if __name__ == '__main__':
    BorderButtonApp().run()
