from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Truffle.kv")


class Truffle(Products):
    """Продукт: Трюфели"""
    def __init__(self, **kwargs):
        super(Truffle, self).__init__(**kwargs)
        self.set_parameters("truffle")
