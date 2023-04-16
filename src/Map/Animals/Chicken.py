from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import AnimalData

Builder.load_file("kv/Animals/Chicken.kv")


class Chicken(Animals):
    """Животное: Курица"""
    def __init__(self, **kwargs):
        super(Chicken, self).__init__(**kwargs)
        self.size = AnimalData.animal_size
        self.set_parameters("chicken")

    def product_drop(self, field):
        self.product_drop_template(field, "egg")
