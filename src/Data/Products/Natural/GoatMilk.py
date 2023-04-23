from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/GoatMilk.kv")


class GoatMilk(Products):
    """Продукт: Козье молоко"""
    def __init__(self, **kwargs):
        super(GoatMilk, self).__init__(**kwargs)
        self.set_parameters("goat milk")
