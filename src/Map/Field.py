from libs.libs import *
from src.Map.Money import Money
import src.Map.Animals.AnimalImports as Animals
import src.Data.Products.ProductsImport as Products

Builder.load_file("kv/Map/Field.kv")


class PlayingField(Label):
    """
        Игровое Поле
    Поля:
        animals: хранит в себе объекты животных, находящихся на поле
        products: хранит в себе объекты продуктов, находящихся на поле
        animals_dict: словарь, хранящий по имени животного представителя класса и количество объектов данного класса на поле
                    (animal_name: [AnimalType(), animal_count)

    """
    animals = list()
    products = list()
    animals_dict = dict()

    def __init__(self, **kwargs):
        super(PlayingField, self).__init__(**kwargs)

    def animal_movement(self, dt):
        """Задает движение всех животных на поле"""
        for animal in self.animals:
            animal.move(self.pos, [self.x + self.size[0], self.y + self.size[1]], self)

    def product_disappearing(self, dt):
        """Обрабатывает процесс исчезновения продуктов на поле"""
        for product in self.products:
            product.current_time += 1
            if product.current_time >= product.life_time:
                self.products.remove(product)
                self.remove_widget(product)

    def create_animal(self, animal_type):
        """Метод, создающий животного по его имени на поле при нажатии на соответствующую кнопку"""
        animal = Animals.animal_dict[animal_type]()
        if Money.get_money() >= animal.cost:
            App.get_running_app().root.gaming_map.update_money(-animal.cost)
            animal.random_place(self.pos, [self.pos[0] + self.size[0], self.pos[1] + self.size[1]])

            self.add_widget(animal)
            self.animals.append(animal)
            if animal.name in self.animals_dict:
                self.animals_dict[animal.name][1] += 1
            else:
                self.animals_dict[animal.name] = [animal, 1]

    def delete_animal(self, animal_name):
        """Метод, удаляющий произвольного животного типа animal_name"""
        for i in range(len(self.animals)):
            if self.animals[i].name == animal_name:
                self.remove_widget(self.animals.pop(i))
                break
        if self.animals_dict[animal_name][1] == 1:
            self.animals_dict.pop(animal_name)
        else:
            self.animals_dict[animal_name][1] -= 1

    def create_product(self, product_type, pos):
        """Метод, создающий продукт на поле"""
        product = Products.product_dict[product_type]()
        product.pos = pos
        self.add_widget(product)
        self.products.append(product)

    def on_touch_down(self, touch):
        """Метод проверяющий нажатие на поле,
        если координаты нажатия лежат в одном из виджетов продуктов поля, то ложит их в склад"""
        for product in self.products:
            if product.collide_point(*touch.pos):
                storage = App.get_running_app().root.gaming_map.storage
                if product.weight + storage.current_weight <= storage.capacity:
                    self.products.remove(product)
                    self.remove_widget(product)
                    storage.add_to_storage(product)
