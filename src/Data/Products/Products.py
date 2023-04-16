from libs.libs import *
from src.Data.Constants import ProductsData, BasicData


class Products(Widget):
    """Базовый класс всех продуктов"""
    name = ""
    price = 0
    weight = 1
    life_time = ProductsData.life_time * BasicData.FPS
    current_time = 0

    def set_parameters(self, product_name):
        """Устанавливает всех параметров объектов типа продукт"""
        self.name = ProductsData.products_dict[product_name][0]
        self.weight = ProductsData.products_dict[product_name][1]
        self.price = ProductsData.products_dict[product_name][2]
        self.size = ProductsData.size
