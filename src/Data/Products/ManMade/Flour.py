from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Flour.kv")


class Flour(Products):
    """Продукт: Мука"""
    def __init__(self, **kwargs):
        super(Flour, self).__init__(**kwargs)
        self.set_parameters("flour")
