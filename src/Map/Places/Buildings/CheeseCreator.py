from libs.libs import *
from src.Map.Places.Buildings.Buildings import LeftBuildings

Builder.load_file("kv/Places/Buildings/CheeseCreator.kv")


class CheeseCreator(LeftBuildings):
    """Фабрика: Сыра"""
    def __init__(self, **kwargs):
        super(CheeseCreator, self).__init__(**kwargs)
        self.product_type = "cheese"
