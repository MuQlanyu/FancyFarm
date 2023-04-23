from libs.libs import *

Builder.load_file("kv/Places/Windows/StorageWindow.kv")


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

    def close(self):
        """Закрывает окно"""
        App.get_running_app().root.gaming_map.storage.is_opened = False
        App.get_running_app().root.gaming_map.game_start()
        self.clear_window()