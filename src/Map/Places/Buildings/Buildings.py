from libs.libs import *
from src.Map.Places.Places import Places
from src.Data.Constants import BuildingsData, ProductsData, BasicData

Builder.load_file("kv/Places/Buildings/Buildings.kv")


class Buildings(Places):
    """
        Абстрактны класс для объектов типа Фабрика(Creator)
        Задает базовое поведение и облегчает создание наследников
    Поля:
        execution_time: Устанавливает время выполнения продукта
    """
    execution_time = BuildingsData.execution_time[0] * BasicData.FPS
    product_type = None
    is_creating = False
    creation_event = None
    creating_time = 0

    def __init__(self, **kwargs):
        super(Buildings, self).__init__(**kwargs)

    def create(self):
        """Определяет создание объектов буз задания местоположения"""
        if self.is_creating: return
        storage = App.get_running_app().root.gaming_map.storage
        for product_name, cnt in BuildingsData.recipes[self.product_type]:
            if product_name not in storage.storage or storage.storage[product_name][1] < cnt:
                return
        for product_name, cnt in BuildingsData.recipes[self.product_type]:
            for i in range(cnt):
                storage.delete_product(product_name)
        self.is_creating = True
        self.creation_event = Clock.schedule_interval(self.creating_process, 1 / BasicData.FPS)

    def creating_process(self, dt):
        pass

    def increase_level(self):
        """Функция повышения уровня"""
        if self.level < len(BuildingsData.execution_time):
            self.execution_time = BuildingsData.execution_time[self.level]
            self.level += 1


class LeftBuildings(Buildings):
    """Класс Фабрик слева от поля"""
    def creating_process(self, dt):
        """Доопределяет создание продуктов: задает местоположение"""
        self.creating_time += 1
        self.create_pb.value = self.creating_time / self.execution_time * 100
        if self.creating_time >= self.execution_time:
            self.is_creating = False
            self.creating_time = 0
            self.create_pb.value = 0
            Clock.unschedule(self.creation_event)
            field = App.get_running_app().root.gaming_map.field
            field.create_product(ProductsData.products_dict[self.product_type][0],
                                 (self.right + self.size[0] / 10, self.y + self.size[1] / 2))


class RightBuildings(Buildings):
    """Класс Фабрик справа от поля"""
    def creating_process(self, dt):
        """Доопределяет создание продуктов: задает местоположение"""
        self.creating_time += 1
        self.create_pb.value = self.creating_time / self.execution_time * 100
        if self.creating_time >= self.execution_time:
            self.is_creating = False
            self.creating_time = 0
            self.create_pb.value = 0
            Clock.unschedule(self.creation_event)
            field = App.get_running_app().root.gaming_map.field
            field.create_product(ProductsData.products_dict[self.product_type][0],
                                 (self.x - self.size[0] / 5, self.y + self.size[1] / 2))
