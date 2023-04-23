from libs.libs import *
from src.Map.Places.Buildings.Buildings import LeftBuildings

Builder.load_file("kv/Places/Buildings/FlourCreator.kv")


class FlourCreator(LeftBuildings):
    """Фабрика: муки"""
    def __init__(self, **kwargs):
        super(FlourCreator, self).__init__(**kwargs)
        self.product_type = "flour"
