from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import AnimalData

Builder.load_file("kv/Animals/Pig.kv")


class Pig(Animals):
    """Животное: Свинья"""
    animal_type = "pig"

    def __init__(self, **kwargs):
        super(Pig, self).__init__(**kwargs)
        self.set_parameters()

    def product_drop(self, field):
        self.product_drop_template(field, "truffle")
