from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Milk.kv")


class Milk(Products):
    """Продукт: Молоко"""
    def __init__(self, **kwargs):
        super(Milk, self).__init__(**kwargs)
        self.set_parameters("milk")
