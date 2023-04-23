from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Cheese.kv")


class Cheese(Products):
    """Продукт: Сыр"""
    def __init__(self, **kwargs):
        super(Cheese, self).__init__(**kwargs)
        self.set_parameters("cheese")
