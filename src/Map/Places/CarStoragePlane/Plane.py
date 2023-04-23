from libs.libs import *
from src.Map.Places.Places import Places
from src.Data.Constants import PlaneData, BasicData
from src.Map.Places.Windows.PlaneWindow import PlaneWindow

Builder.load_file("kv/Places/Plane.kv")


class Plane(Places):
    capacity = PlaneData.capacity[0]
    flying_time = PlaneData.riding_time[0] * BasicData.FPS
    flying_event = None
    is_opened = False
    is_flying = False
    current_weight = 0
    current_price = 0
    current_time = 0

    def __init__(self, **kwargs):
        """Создает машину и её окно"""
        super(Plane, self).__init__(**kwargs)
        self.window = PlaneWindow()
        self.window.pos = PlaneData.window_pos
        self.window.size = PlaneData.window_size

    def increase_level(self):
        """Функция повышения уровня"""
        if self.level < len(PlaneData.capacity):
            self.capacity = PlaneData.capacity[self.level]
            self.flying_time = PlaneData.riding_time[self.level]
            self.level += 1

    def add_item_to_list(self, item, price):
        """Функция добавления продуктов в машину"""
        self.window.buy_list.append(item)
        self.current_weight += item.weight
        self.current_price += price
        self.window.label.text = str(self.current_weight) + " / " + str(self.capacity)

    def remove_item_from_list(self, item, price):
        for current_item in self.window.buy_list:
            if current_item.name == item.name:
                self.window.buy_list.remove(current_item)
                self.current_weight -= item.weight
                self.current_price -= price
                self.window.label.text = str(self.current_weight) + " / " + str(self.capacity)
                return True
        return False

    def on_touch_down(self, touch):
        """
            Проверяет нажатие на виджет машины:
          1)Если машины в пути, то ничего не произойдет
          2)Если окно не открыто, то откроет его
        """
        if self.button.collide_point(*touch.pos):
            if not self.is_opened and not self.is_flying:
                self.is_opened = True
                self.current_weight = 0
                self.current_price = 0
                self.window.buy_list.clear()
                App.get_running_app().root.gaming_map.game_stop()
                App.get_running_app().root.gaming_map.add_widget(self.window.set_product_list())

    def drop_products(self):
        field = App.get_running_app().root.gaming_map.field
        bottom_left = field.pos
        top_right = [field.pos[0] + field.size[0], field.pos[1] + field.size[1]]
        for product in self.window.buy_list:
            product.x = randint(int(bottom_left[0]) + 1, int(top_right[0] - self.size[0]) - 1)
            product.y = randint(int(bottom_left[1]) + 1, int(top_right[1] - self.size[1]) - 1)
            field.add_widget(product)
            field.products.append(product)

    def flying(self, dt):
        if not App.get_running_app().root.gaming_map.is_stopped:
            gmap = App.get_running_app().root.gaming_map
            self.current_time += 1
            gmap.plane_progress_bar.value = (self.flying_time / 2 - abs(
                self.current_time - self.flying_time / 2)) / self.flying_time * 200
            if self.current_time >= self.flying_time:
                self.window.text = "Buy"
                self.drop_products()

                self.current_price = 0
                self.current_weight = 0
                self.current_time = 0
                self.is_flying = False
                Clock.unschedule(self.flying_event)
