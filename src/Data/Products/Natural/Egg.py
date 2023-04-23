from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Egg.kv")


class Egg(Products):
    """Продукт: Яйцо"""
    def __init__(self, **kwargs):
        super(Egg, self).__init__(**kwargs)
        self.set_parameters("egg")
