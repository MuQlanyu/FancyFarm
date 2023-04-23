from libs.libs import *
from src.Map.Places.Places import Places
from src.Data.Constants import CarData, BasicData
from src.Map.Places.Windows.CarWindow import CarWindow

Builder.load_file("kv/Places/Car.kv")


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
    riding_event = None
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
          2)Если окно не открыто, то откроет его
        """
        if self.button.collide_point(*touch.pos):
            if not self.is_opened and not self.is_riding:
                self.is_opened = True
                self.current_sum = 0
                self.current_weight = 0
                App.get_running_app().root.gaming_map.game_stop()
                App.get_running_app().root.gaming_map.add_widget(self.window.set_product_list())

    def add_item_to_list(self, item):
        """Функция добавления продуктов в машину"""
        self.window.sell_list.append(item)
        self.current_weight += item.weight
        self.current_sum += item.price
        self.window.label.text = str(self.current_weight) + " / " + str(self.capacity)

    def remove_item_from_list(self, item):
        for current_item in self.window.sell_list:
            if current_item.name == item.name:
                self.window.sell_list.remove(current_item)
                self.current_weight -= item.weight
                self.current_sum -= item.price
                self.window.label.text = str(self.current_weight) + " / " + str(self.capacity)
                return True
        return False

    def riding(self, dt):
        """Описывает поведение машины в пути и при его окончании"""
        if not App.get_running_app().root.gaming_map.is_stopped:
            gmap = App.get_running_app().root.gaming_map
            self.current_time += 1
            gmap.car_progress_bar.value = (self.riding_time / 2 - abs(
                self.current_time - self.riding_time / 2)) / self.riding_time * 200
            if self.current_time >= self.riding_time:
                gmap.update_money(self.current_sum)
                self.window.text = "Sell"

                self.current_sum = 0
                self.current_weight = 0
                self.current_time = 0
                self.is_riding = False
                Clock.unschedule(self.riding_event)
