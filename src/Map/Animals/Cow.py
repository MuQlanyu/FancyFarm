from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import AnimalData

Builder.load_file("kv/Animals/Cow.kv")


class Cow(Animals):
    """Животное: Корова"""
    animal_type = "cow"

    def __init__(self, **kwargs):
        super(Cow, self).__init__(**kwargs)
        self.set_parameters()

    def product_drop(self, field):
        self.product_drop_template(field, "milk")
