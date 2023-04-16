from kivy.config import Config
from src.Data.Constants import BasicData

Config.set('graphics', 'width', str(BasicData.window_width))
Config.set('graphics', 'height', str(BasicData.window_height))
Config.set('graphics', 'resizable', False)
Config.write()

from libs.libs import *
from src.Menu import Menu


class FancyFarmApp(App):

    def build(self):
        return Menu()


FancyFarmApp().run()
