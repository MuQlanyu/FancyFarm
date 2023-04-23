from libs.libs import *
from src.Data.Constants import BasicData
from src.Map.Animals.Animals import Animals
from src.Map.Animals.AnimalImports import animal_dict
from src.Map.Places.Windows.StorageWindow import StorageProduct
from src.Data.Products.ProductsImport import product_dict


Builder.load_file("kv/Places/Windows/CarWindow.kv")


class ProductWidget(StorageProduct):
    """Виджет продуктов на складе"""

    def sell_product(self):
        """Обрабатывает нажатие на кнопку продажи продукта"""
        product = App.get_running_app().root.gaming_map.storage.storage[self.pr_name.text][0]
        car = App.get_running_app().root.gaming_map.car
        if product.weight + car.current_weight <= car.capacity and int(self.pr_cnt.text) > 0:
            car.add_item_to_list(product)
            self.pr_cnt.text = str(int(self.pr_cnt.text) - 1)

    def back_product(self):
        product = product_dict[self.pr_name.text]()
        if App.get_running_app().root.gaming_map.car.remove_item_from_list(product):
            self.pr_cnt.text = str(int(self.pr_cnt.text) + 1)


class AnimalProduct(BoxLayout):
    """Виджет продуктов на пало"""

    def set_parameters(self, animal, cnt):
        """Задает характеристики виджета"""
        self.an_name.text = animal.name
        self.an_price.text = str(animal.price)
        self.an_cnt.text = str(cnt)
        return self

    def sell_animal(self):
        """Обрабатывает нажатие на кнопку продажи животного"""
        animal = App.get_running_app().root.gaming_map.field.animals_dict[self.an_name.text][0]
        car = App.get_running_app().root.gaming_map.car
        if animal.weight + car.current_weight <= car.capacity and int(self.an_cnt.text) > 0:
            car.add_item_to_list(animal)
            self.an_cnt.text = str(int(self.an_cnt.text) - 1)

    def back_animal(self):
        animal = animal_dict[self.an_name.text]()
        if App.get_running_app().root.gaming_map.car.remove_item_from_list(animal):
            self.an_cnt.text = str(int(self.an_cnt.text) + 1)


class CarWindow(BoxLayout):
    """
        Окно машины(открывается/закрывается при нажатии на виджет машины)
    Поля:
        sell_list: список элементов в машине
    """
    sell_list = list()

    def __init__(self, **kwargs):
        super(CarWindow, self).__init__(**kwargs)

    def set_product_list(self):
        """
            Заполняет окно виджетами: CarProduct, AnimalProduct
        Магические константы:
          1)Максимальный размер поля продуктов, при котором виджеты не меняют свой размер
          2)Максимальный размер поля животных, при котором виджеты не меняют свой размер
        """
        storage = App.get_running_app().root.gaming_map.storage.storage
        animals = App.get_running_app().root.gaming_map.field.animals_dict
        ind = 1
        for product, num in storage.values():
            self.pr_list.add_widget(ProductWidget().set_parameters(product, num, ind))
            ind += 1
        if ind < 16:  # Маг константа 1
            self.pr_list.add_widget(Widget(size_hint_y=(16 - ind) / 10))
        ind = 1
        for animal, num in animals.values():
            self.an_list.add_widget(AnimalProduct().set_parameters(animal, num))
            ind += 1
        if ind < 11:  # Маг константа 2
            self.an_list.add_widget(Widget(size_hint_y=(11 - ind) / 10))
        return self

    def sell_all(self):
        """Обрабатывает кнопку продажи всех элементов в sell_list"""
        if not self.sell_list: return
        for item in self.sell_list:
            if isinstance(item, Animals):
                App.get_running_app().root.gaming_map.field.delete_animal(item.name)
            else:
                App.get_running_app().root.gaming_map.storage.delete_product(item.name)
        self.sell_list.clear()
        self.sell_button.text = "On the way"
        self.label.text = "Weight"
        car = App.get_running_app().root.gaming_map.car
        car.riding_event = Clock.schedule_interval(car.riding, 1 / BasicData.FPS)

    def clear_window(self):
        """Очищает окно"""
        self.pr_list.clear_widgets()
        self.an_list.clear_widgets()
        self.label.text = "Weight"
        App.get_running_app().root.gaming_map.remove_widget(self)

    def close(self):
        """Закрывает окно"""
        App.get_running_app().root.gaming_map.car.is_opened = False
        App.get_running_app().root.gaming_map.game_start()
        self.clear_window()
