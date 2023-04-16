from libs.libs import *
from src.Map.Places.Buildings.Buildings import LeftBuildings

Builder.load_file("kv/Places/Buildings/OilCreator.kv")


class OilCreator(LeftBuildings):
    """Фабрика: Козьего масла"""
    def __init__(self, **kwargs):
        super(OilCreator, self).__init__(**kwargs)

    def create(self):
        self.create_template("goat oil")
