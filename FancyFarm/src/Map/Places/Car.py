from libs.libs import *
from src.Map.Places.Places import Places
from src.Data.Constants import CarData, BasicData
from src.Map.Animals.Animals import Animals
from src.Map.Places.Storage import StorageProduct

Builder.load_file("kv/Places/Car.kv")


class CarProduct(StorageProduct):
    """Виджет продуктов на складе"""

    def sell_product(self):
        """Обрабатывает нажатие на кнопку продажи продукта"""
        product = App.get_running_app().root.gaming_map.storage.storage[self.pr_name.text][0]
        car = App.get_running_app().root.gaming_map.car
        if product.weight + car.current_weight <= car.capacity and int(self.pr_cnt.text) > 0:
            car.add_item_to_list(product)
            self.pr_cnt.text = str(int(self.pr_cnt.text) - 1)


class AnimalProduct(BoxLayout):
    """Виджет продуктов на пало"""

    def set_parameters(self, animal, cnt):
        """Задает характеристики виджета"""
        self.an_name.text = animal.name
        self.an_price.text = str(animal.price)
        self.an_cnt.text = str(cnt)
        return self

    def sell_product(self):
        """Обрабатывает нажатие на кнопку продажи животного"""
        animal = App.get_running_app().root.gaming_map.field.animals_dict[self.an_name.text][0]
        car = App.get_running_app().root.gaming_map.car
        if animal.weight + car.current_weight <= car.capacity and int(self.an_cnt.text) > 0:
            car.add_item_to_list(animal)
            self.an_cnt.text = str(int(self.an_cnt.text) - 1)


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
            self.pr_list.add_widget(CarProduct().set_parameters(product, num, ind))
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
        App.get_running_app().root.gaming_map.remove_widget(self)


class Car(Places):
    """
        Класс Машины
    Поля:
        capacity: Грузоподъемность машины
        riding_time: Время в пути
        window: Окно, открывающееся при нажатии на виджет машины
        is_opened: Показывает, открыто ли окно
        is_riding: Показывает, в пути ли машина
        current_weight: Загруженность машины на данный момент
        current_sum: Сумма загруженного товара
        current_time: Время машины в пути
    """
    capacity = CarData.capacity[0]
    riding_time = CarData.riding_time[0] * BasicData.FPS
    is_opened = False
    is_riding = False
    current_weight = 0
    current_sum = 0
    current_time = 0

    def __init__(self, **kwargs):
        """Создает машину и её окно"""
        super(Car, self).__init__(**kwargs)
        self.window = CarWindow()
        self.window.pos = CarData.window_pos
        self.window.size = CarData.window_size
        self.window.sell_label = "0 / " + str(self.capacity)

    def increase_level(self):
        """Функция повышения уровня"""
        if self.level < len(CarData.capacity):
            self.capacity = CarData.capacity[self.level]
            self.riding_time = CarData.riding_time[self.level]
            self.level += 1

    def on_touch_down(self, touch):
        """
            Проверяет нажатие на виджет машины:
          1)Если машины в пути, то ничего не произойдет
          2)Если окно уже открыто, то закроет его
          3)Если окно не открыто, то откроет его
        """
        if self.button.collide_point(*touch.pos):
            if not self.is_opened and not self.is_riding:
                self.is_opened = True
                App.get_running_app().root.gaming_map.game_stop()
                App.get_running_app().root.gaming_map.add_widget(self.window.set_product_list())
            elif self.is_opened:
                self.is_opened = False
                App.get_running_app().root.gaming_map.game_start()
                self.window.clear_window()

    def add_item_to_list(self, item):
        """Функция добавления продуктов в машину"""
        self.window.sell_list.append(item)
        self.current_weight += item.weight
        self.current_sum += item.price
        self.window.label.text = str(self.current_weight) + " / " + str(self.capacity)

    def riding(self, dt):
        """Описывает поведение машины в пути и при его окончании"""
        if not App.get_running_app().root.gaming_map.is_stopped:
            self.current_time += 1
            if self.current_time >= self.riding_time:
                App.get_running_app().root.gaming_map.update_money(self.current_sum)
                self.window.text = "Sell"

                self.current_sum = 0
                self.current_weight = 0
                self.current_time = 0
                self.is_riding = False
                Clock.unschedule(self.riding)
