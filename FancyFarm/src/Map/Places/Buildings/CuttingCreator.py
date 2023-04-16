from libs.libs import *
from src.Map.Places.Buildings.Buildings import RightBuildings

Builder.load_file("kv/Places/Buildings/CuttingCreator.kv")


class CuttingCreator(RightBuildings):
    """Фабрика: Нарезка трюфелей"""
    def __init__(self, **kwargs):
        super(CuttingCreator, self).__init__(**kwargs)

    def create(self):
        self.create_template("truffle сutting")
