from libs.libs import *
from src.Data.Products.Products import Products

Builder.load_file("kv/Products/Bearina.kv")


class Bearina(Products):
    """Продукт: Медвежатина"""
    def __init__(self, **kwargs):
        super(Bearina, self).__init__(**kwargs)
        self.set_parameters("bearina")
