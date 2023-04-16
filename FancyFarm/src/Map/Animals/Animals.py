from libs.libs import *
from src.Data.Constants import AnimalData, BasicData
import src.Data.Products.ProductsImport as Products


class Animals(Widget):
    """
        Абстрактный класс для объектов типа: животное
        Задает базовое поведение наследников
    Поля:
        name: имя животного
        cost: цена приобретения животного
        price: цена продажи животного
        weight: вес животного
        speed: скорость животного
        * В данном случае под временем время подразумевается количество кадров(real_time * FPS)
        change_dir_time: поле, отображающее время до следующего изменения направления и скорости
                        (если до этого животного не столкнется с препятствием)
        product_timer: время с последнего момента создания продукта
        drop_frequency: период создания продукта
    """
    name = None
    cost = None
    price = None
    weight = None

    speed = [None, None]
    change_dir_time = 0

    product_timer = 0
    drop_frequency = 0

    def __int__(self, **kwargs):
        super(Animals, self).__init__(**kwargs)

    def product_drop_template(self, field, product_name):
        """
            Шаблон для создания продуктов животным
        Цель: Облегчить объявление типов животных
        """
        self.product_timer += 1
        if self.product_timer >= self.drop_frequency:
            self.product_timer = 0
            product = Products.product_dict[product_name]()
            product.pos = (self.x + self.size[0] / 2 - product.size[0] / 2,
                           self.y + self.size[1] / 2 - product.size[1] / 2)
            field.add_widget(product)
            field.products.append(product)

    def set_parameters(self, animal_name):
        """Устанавливает все параметры объектов типа животное"""
        self.name = AnimalData.animal_dict[animal_name][0]
        self.weight = AnimalData.animal_dict[animal_name][1]
        self.cost = AnimalData.animal_dict[animal_name][2]
        self.price = AnimalData.animal_dict[animal_name][3]
        self.drop_frequency = AnimalData.animal_dict[animal_name][4] * BasicData.FPS
        self.update_speed([0, 0])
        self.speed = self.speed.copy()

    def product_drop(self, field):
        """Виртуальный метод создания продукта"""
        pass

    def set_change_dir_time(self):
        """Устанавливает change_dir_time"""
        self.change_dir_time = BasicData.FPS
        self.change_dir_time *= randint(AnimalData.animal_change_dir_max_interval * 7,
                                        AnimalData.animal_change_dir_max_interval * 10) / 10

    def random_place(self, bottom_left, top_right):
        """Устанавливает рандомное место спавна животного при его создании"""
        self.x = randint(int(bottom_left[0]) + 1, int(top_right[0] - self.size[0]) - 1)
        self.y = randint(int(bottom_left[1]) + 1, int(top_right[1] - self.size[1]) - 1)

    def update_speed(self, direction):
        """
              Меняет скорость и направление при:
          1)Столкновении животного с границами поля
          2)При обнулении change_dir_time
          3)При создании животного
          В случае пункта 1, также меняет направление от границы
        """
        if direction[0] == 0:
            direction[0] = -1 if randint(0, 1) == 0 else 1
        if direction[1] == 0:
            direction[1] = -1 if randint(0, 1) == 0 else 1
        self.speed[0] = direction[0] * randint(int(AnimalData.animal_max_speed * 7000),
                                               int(AnimalData.animal_max_speed * 70000)) / 70000
        self.speed[1] = direction[1] * randint(int(AnimalData.animal_max_speed * 7000),
                                               int(AnimalData.animal_max_speed * 70000)) / 70000
        self.set_change_dir_time()

    def out_of_bound(self, bottom_left, top_right, change_dir, is_y):
        """Проверка на выход за границы"""
        if self.pos[is_y] < bottom_left[is_y] or self.pos[is_y] + self.size[is_y] > top_right[is_y]:
            if self.pos[is_y] < bottom_left[is_y] and self.speed[is_y] <= 0:
                change_dir[is_y] = 1
            if self.pos[is_y] + self.size[is_y] > top_right[is_y] and self.speed[is_y] >= 0:
                change_dir[is_y] = -1

    def move(self, bottom_left, top_right, field):
        """
              Метод движения животных
            Что делает
          1)Выполняет процесс создания продукта (self.product_drop(field))
          2)Меняет положение животного на поле в зависимости от скорости
          3)Меняет скорость и направление при столкновении с границей или
            при обнулении change_dir_time
        """
        self.product_drop(field)
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        change_dir = [0, 0]
        self.out_of_bound(bottom_left, top_right, change_dir, 0)
        self.out_of_bound(bottom_left, top_right, change_dir, 1)
        if change_dir[0] != 0 or change_dir[1] != 0:
            self.update_speed(change_dir)

        self.change_dir_time -= 1
        if self.change_dir_time <= 0:
            self.set_change_dir_time()
            self.update_speed([0, 0])
