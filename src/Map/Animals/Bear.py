# Не успел реализовать
from libs.libs import *
from src.Map.Animals.Animals import Animals
from src.Data.Constants import BearData
import src.Data.Products.ProductsImport as Products

Builder.load_file("kv/Animals/Bear.kv")


class Bear(Animals):
    """Животное: Медведь"""
    MaxHP = BearData.hp[0]
    HP = BearData.hp[0]
    color = BearData.color
    animal_type = "bear"

    def __init__(self, **kwargs):
        super(Bear, self).__init__(**kwargs)
        self.set_parameters()

    def set_parameters(self):
        self.name = self.animal_type
        self.drop_frequency = 1e9
        self.size = BearData.size
        self.update_speed([0, 0])
        self.speed = self.speed.copy()

    def product_drop(self, field):
        self.product_drop_template(field, "bearina")

    def decrease_life(self):
        self.HP -= BearData.click_power
        self.check_if_dead()

    def check_if_dead(self):
        if self.HP > 0: return
        field = App.get_running_app().root.gaming_map.field
        product = Products.product_dict["bearina"]()
        product.pos = (self.x + self.size[0] / 2 - product.size[0] / 2,
                       self.y + self.size[1] / 2 - product.size[1] / 2)
        field.add_widget(product)
        field.products.append(product)
        field.bears.remove(self)
        field.remove_widget(self)
