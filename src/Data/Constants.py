class BasicData:
    """Базовы константы"""
    window_height = 800
    window_width = 1200

    FPS = 60

    starting_amount_of_money = 100000  # начальная сумма денег


class FieldData:
    """Константы поля"""
    field_size_hint = (1 / 1.6, 0.8 / 1.15)


class AnimalData:
    """Константы животных"""
    animal_max_speed = (BasicData.window_width + BasicData.window_height) / (15 * BasicData.FPS)
    animal_change_dir_max_interval = 5

    # key: [name, weight, cost, sell_price, frequency]
    animal_dict = {
        "chicken": ["chicken", 20, 100, 50, 12],
        "goat": ["goat", 30, 1000, 500, 15],
        "cow": ["cow", 100, 10000, 5000, 17],
        "pig": ["pig", 200, 50000, 10000, 20]
    }

    animal_size = {
        "chicken": (100, 90),
        "goat": (130, 120),
        "cow": (170, 105),
        "pig": (150, 85)
    }


class ProductsData:
    """Константы продуктов"""
    life_time = 7

    # key : [name, weight, price, size]
    products_dict = {
        "bearina": ["bearina", 50, 100],
        "egg": ["egg", 5, 10],
        "goat milk": ["goat milk", 10, 100],
        "milk": ["milk", 20, 1000],
        "truffle": ["truffle", 30, 7000],
        "flour": ["flour", 5, 20],
        "goat oil": ["goat oil", 15, 250],
        "cheese": ["cheese", 30, 3000],
        "truffle сutting": ["truffle сutting", 30, 10000]
    }


class StorageData:
    """Константы склада"""
    capacity = [200, 400, 600, 800, 1200]
    window_pos = (BasicData.window_width / 5, BasicData.window_height / 6)
    window_size = (BasicData.window_width * 1.6, BasicData.window_height * 1.6)


class CarData:
    """Константы машины"""
    capacity = [100, 200, 300, 400, 600]
    riding_time = [30, 20, 15, 10, 5]
    window_pos = (BasicData.window_width / 5, BasicData.window_height / 6)
    window_size = (BasicData.window_width * 1.6, BasicData.window_height * 1.6)


class PlaneData:
    """Константы самолета"""
    capacity = [50, 100, 150, 200, 300]
    riding_time = [10, 20, 15, 10, 5]
    window_pos = (BasicData.window_width / 5, BasicData.window_height / 6)
    window_size = (BasicData.window_width * 1.6, BasicData.window_height * 1.6)

    stock = [["egg", 15]]


class BuildingsData:
    """Константы зданий(заводиков)"""
    execution_time = [15, 10, 5]

    # Flour creator
    recipes = {
        "flour": [["egg", 1]],
        "goat oil": [["goat milk", 1]],
        "cheese": [["milk", 1]],
        "truffle сutting": [["truffle", 1]]
    }


class BearData:
    """Константы медведя"""
    click_power = 50
    hp = [100, 200, 400]

    size = (200, 110)

    color = [46 / 255, 32 / 255, 1 / 255, 1]

    spawning_accuracy = 1e7
    spawning_chance = [0.3, 0.4, 0.3]
    spawning_cycle = 40
    spawning_cycle_deviation = 0.3


class ImageData:
    image_frequency = BasicData.FPS / 8

    images_dict = {
        "chicken": [["images/chicken/left1.png", "images/chicken/left2.png",
                     "images/chicken/left3.png", "images/chicken/left4.png", ],
                    ["images/chicken/right1.png", "images/chicken/right2.png",
                     "images/chicken/right3.png", "images/chicken/right4.png", ]],
        "goat": [["images/goat/left1.png", "images/goat/left2.png",
                  "images/goat/left3.png", "images/goat/left4.png", ],
                 ["images/goat/right1.png", "images/goat/right2.png",
                  "images/goat/right3.png", "images/goat/right4.png", ]],
        "cow": [["images/cow/left1.png", "images/cow/left2.png",
                 "images/cow/left3.png", "images/cow/left4.png", ],
                ["images/cow/right1.png", "images/cow/right2.png",
                 "images/cow/right3.png", "images/cow/right4.png", ]],
        "pig": [["images/pig/left1.png", "images/pig/left2.png",
                 "images/pig/left3.png", "images/pig/left4.png", ],
                ["images/pig/right1.png", "images/pig/right2.png",
                 "images/pig/right3.png", "images/pig/right4.png", ]],
        "bear": [["images/bear/left1.png", "images/bear/left2.png",
                 "images/bear/left3.png", "images/bear/left4.png", ],
                ["images/bear/right1.png", "images/bear/right2.png",
                 "images/bear/right3.png", "images/bear/right4.png", ]],
    }
