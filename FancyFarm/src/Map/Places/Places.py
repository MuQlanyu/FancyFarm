from libs.libs import *


class Places(BoxLayout):
    """
        Абстрактны класс всех зданий:
      1)Фабрик
      2)Машина
      3)Склад
      4)Самолет
    """
    level = 0

    def __init__(self, **kwargs):
        super(Places, self).__init__(**kwargs)

    def increase_level(self):
        """Виртуальная функция повышения уровня"""
        pass
