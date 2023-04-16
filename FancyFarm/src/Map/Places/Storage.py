from libs.libs import *
from src.Data.Constants import StorageData
from src.Map.Places.Places import Places

Builder.load_file("kv/Places/Storage.kv")


class StorageProduct(BoxLayout):
    """Виджет продуктов на складе"""

    def __init__(self, **kwargs):
        super(StorageProduct, self).__init__(**kwargs)

    def set_parameters(self, product, cnt, number):
        """Устанавливает параметры виджета"""
        self.pr_number.text = str(number)
        self.pr_name.text = product.name
        self.pr_price.text = str(product.price)
        self.pr_cnt.text = str(cnt)
        self.total_price.text = str(product.price * cnt)
        return self


class StorageWindow(BoxLayout):
    """
        Окно Склада(открывается/закрывается при нажатии на виджет склада)
    """

    def __init__(self, **kwargs):
        super(StorageWindow, self).__init__(**kwargs)

    def set_product_list(self, storage):
        """
            Заполняет окно виджетами: StorageProduct(объекты на складе)
        Магические константы:
          1)Максимальный размер поля продуктов, при котором виджеты не меняют свой размер
        """
        ind = 1
        for product, num in storage.values():
            self.pr_list.add_widget(StorageProduct().set_parameters(product, num, ind))
            ind += 1
        if ind < 16:  # Маг константа 1
            self.pr_list.add_widget(Widget(size_hint_y=(16 - ind) / 10))
        return self

    def clear_window(self):
        """Очищает окно"""
        self.pr_list.clear_widgets()
        App.get_running_app().root.gaming_map.remove_widget(self)


class Storage(Places):
    """
        Класс склада
    Поля:
        capacity: Вместимость склада
        current_weight: Нынешний вес объектов склада
        storage: Словарь объектов склада
        is_opened: Показывает открыто ли окно склада
        window: Окно, открывающееся при нажатии на виджет машины
    """
    capacity = StorageData.capacity[0]
    current_weight = 0
    storage = dict()
    is_opened = False

    def __init__(self, **kwargs):
        """Склад машину и его окно"""
        super(Storage, self).__init__(**kwargs)
        self.window = StorageWindow()
        self.window.pos = StorageData.window_pos
        self.window.size = StorageData.window_size

    def increase_level(self):
        """Функция повышения уровня"""
        if self.level < len(StorageData.capacity):
            self.capacity = StorageData.capacity[self.level]
            self.level += 1

    def add_to_storage(self, product):
        """Метод добавления объектов в склад"""
        if product.name in self.storage:
            self.storage[product.name][1] += 1
        else:
            self.storage[product.name] = [product, 1]
        self.current_weight += product.weight
        self.storage_button.text = str(self.current_weight) + ' / ' + str(self.capacity)

    def on_touch_down(self, touch):
        """
            Проверяет нажатие на виджет машины:
          1)Если машины в пути, то ничего не произойдет
          2)Если окно уже открыто, то закроет его
          3)Если окно не открыто, то откроет его
        """
        if self.collide_point(*touch.pos):
            if not self.is_opened:
                self.is_opened = True
                App.get_running_app().root.gaming_map.game_stop()
                App.get_running_app().root.gaming_map.add_widget(self.window.set_product_list(self.storage))
            else:
                self.is_opened = False
                App.get_running_app().root.gaming_map.game_start()
                self.window.clear_window()

    def delete_product(self, product_name):
        """Метод удаления объектов со склада"""
        self.current_weight -= self.storage[product_name][0].weight
        if self.storage[product_name][1] == 1:
            self.storage.pop(product_name)
        else:
            self.storage[product_name][1] -= 1
        self.storage_button.text = str(self.current_weight) + ' / ' + str(self.capacity)
