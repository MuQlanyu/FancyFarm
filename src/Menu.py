from libs.libs import *
from src.Map.Map import Map

Builder.load_file("kv/Menu.kv")


class Options(BoxLayout):
    """Класс Настроек"""

    def back_to_menu(self):
        """Функция переключения в меню"""
        self.clear_widgets()
        self.add_widget(Menu())


class Menu(BoxLayout):
    """
        Класс Меню
    Поля:
        gaming_map: объект игры
    """
    gaming_map = None

    def change_place(self, place):
        """Меняет текущее окно на place"""
        self.clear_widgets()
        self.add_widget(place)

    def menu(self):
        self.change_place(Menu())

    def game(self):
        """Запускает игру"""
        self.gaming_map = Map()
        self.change_place(self.gaming_map)

    def options(self):
        """Открывает настройки"""
        self.change_place(Options())

    @staticmethod
    def exit():
        """Закрывает игру"""
        App.get_running_app().stop()
        Window.close()
