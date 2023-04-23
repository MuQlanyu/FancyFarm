from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import AnimalData

Builder.load_file("kv/Animals/Goat.kv")


class Goat(Animals):
    """Животное: Коза"""
    animal_type = "goat"

    def __init__(self, **kwargs):
        super(Goat, self).__init__(**kwargs)
        self.set_parameters()

    def product_drop(self, field):
        self.product_drop_template(field, "goat milk")
