from libs.libs import *
from src.Map.Places.Places import Places
from src.Data.Constants import BuildingsData, ProductsData

Builder.load_file("kv/Places/Buildings/Buildings.kv")


class Buildings(Places):
    """
        Абстрактны класс для объектов типа Фабрика(Creator)
        Задает базовое поведение и облегчает создание наследников
    Поля:
        execution_time: Устанавливает время выполнения продукта
    """
    execution_time = BuildingsData.execution_time[0]

    def __init__(self, **kwargs):
        super(Buildings, self).__init__(**kwargs)

    @staticmethod
    def create_template_base(recipe):
        """Определяет создание объектов буз задания местоположения"""
        storage = App.get_running_app().root.gaming_map.storage
        for product_name, cnt in BuildingsData.recipes[recipe]:
            if product_name not in storage.storage or storage.storage[product_name][1] < cnt:
                return
        for product_name, cnt in BuildingsData.recipes[recipe]:
            for i in range(cnt):
                storage.delete_product(product_name)

    def create(self):
        """Виртуальная функция создающая продукты"""
        pass

    def increase_level(self):
        """Функция повышения уровня"""
        if self.level < len(BuildingsData.execution_time):
            self.execution_time = BuildingsData.execution_time[self.level]
            self.level += 1


class LeftBuildings(Buildings):
    """Класс Фабрик слева от поля"""
    def create_template(self, recipe):
        """Доопределяет создание продуктов: задает местоположение"""
        self.create_template_base(recipe)
        field = App.get_running_app().root.gaming_map.field
        field.create_product(ProductsData.products_dict[recipe][0],
                             (self.right + self.size[0] / 10, self.y + self.size[1] / 2))


class RightBuildings(Buildings):
    """Класс Фабрик справа от поля"""
    def create_template(self, recipe):
        """Доопределяет создание продуктов: задает местоположение"""
        self.create_template_base(recipe)
        field = App.get_running_app().root.gaming_map.field
        field.create_product(ProductsData.products_dict[recipe][0],
                             (self.x - self.size[0] / 10, self.y + self.size[1] / 2))
