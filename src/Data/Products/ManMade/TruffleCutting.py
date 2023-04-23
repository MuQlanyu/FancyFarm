from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/TruffleCutting.kv")


class TruffleCutting(Products):
    """Продукт: Нарезка трюфелей"""
    def __init__(self, **kwargs):
        super(TruffleCutting, self).__init__(**kwargs)
        self.set_parameters("truffle сutting")
