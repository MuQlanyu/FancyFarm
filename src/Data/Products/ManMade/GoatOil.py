from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/GoatOil.kv")


class GoatOil(Products):
    """Продукт: Козье масло"""
    def __init__(self, **kwargs):
        super(GoatOil, self).__init__(**kwargs)
        self.set_parameters("goat oil")
