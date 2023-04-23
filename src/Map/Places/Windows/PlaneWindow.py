from libs.libs import *
from src.Data.Constants import PlaneData, BasicData
from src.Data.Products.ProductsImport import product_dict

Builder.load_file("kv/Places/Windows/PlaneWindow.kv")


class PlaneProduct(BoxLayout):

    def __init__(self, **kwargs):
        super(PlaneProduct, self).__init__(**kwargs)

    def set_parameters(self, product_name, cost, number):
        """Устанавливает параметры виджета"""
        self.pr_number.text = str(number)
        self.pr_name.text = product_name
        self.pr_price.text = str(cost)
        return self

    def buy_product(self):
        """Обрабатывает нажатие на кнопку продажи продукта"""
        product = product_dict[self.pr_name.text]()
        plane = App.get_running_app().root.gaming_map.plane
        if product.weight + plane.current_weight <= plane.capacity:
            plane.add_item_to_list(product, int(self.pr_price.text))

    def return_product(self):
        product = product_dict[self.pr_name.text]()
        App.get_running_app().root.gaming_map.plane.remove_item_from_list(product, int(self.pr_price.text))


class PlaneWindow(BoxLayout):
    buy_list = list()

    def __init__(self, **kwargs):
        super(PlaneWindow, self).__init__(**kwargs)

    def set_product_list(self):
        """
            Заполняет окно виджетами: StorageProduct(объекты на складе)
        Магические константы:

          1)Максимальный размер поля продуктов, при котором виджеты не меняют свой размер
        """
        ind = 1
        for product_name, cost in PlaneData.stock:
            self.pr_list.add_widget(PlaneProduct().set_parameters(product_name, cost, ind))
            ind += 1
        if ind < 16:  # Маг константа 1
            self.pr_list.add_widget(Widget(size_hint_y=(16 - ind) / 10))
        return self

    def buy_all(self):
        if not self.buy_list: return
        self.buy_button.text = "On the way"
        self.label.text = "Weight"
        plane = App.get_running_app().root.gaming_map.plane
        gmap = App.get_running_app().root.gaming_map
        gmap.update_money(-gmap.plane.current_price)
        plane.flying_event = Clock.schedule_interval(plane.flying, 1 / BasicData.FPS)

    def clear_window(self):
        """Очищает окно"""
        self.pr_list.clear_widgets()
        App.get_running_app().root.gaming_map.remove_widget(self)

    def close(self):
        """Закрывает окно"""
        App.get_running_app().root.gaming_map.plane.is_opened = False
        App.get_running_app().root.gaming_map.game_start()
        self.clear_window()
