# Не успел реализовать
from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import AnimalData


class Bear(Animals):
    """Животное: Медведь"""
    def __init__(self, **kwargs):
        super(Bear, self).__init__(**kwargs)
        self.size = AnimalData.bear_size
        self.set_parameters("bear")

    def product_drop(self, field):
        self.product_drop_template(field, "egg")
