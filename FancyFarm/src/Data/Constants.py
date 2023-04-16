class BasicData:
    """Базовы константы"""
    window_height = 800
    window_width = 1200

    FPS = 60

    starting_amount_of_money = 500  # начальная сумма денег


class FieldData:
    """Константы поля"""
    field_size_hint = (1 / 1.6, 0.8 / 1.15)


class AnimalData:
    """Константы животных"""
    animal_max_speed = (BasicData.window_width + BasicData.window_height) / (15 * BasicData.FPS)
    animal_change_dir_max_interval = 5
    animal_size_hint = 0.08  # 0.1 * window_width
    animal_size = (BasicData.window_width * animal_size_hint,
                   BasicData.window_width * animal_size_hint)

    # key: [name, weight, cost, sell_price, frequency]
    animal_dict = {
        "chicken": ["chicken", 20, 100, 50, 10],
        "goat": ["goat", 30, 1000, 500, 15],
        "cow": ["cow", 100, 10000, 5000, 20],
        "pig": ["pig", 200, 50000, 10000, 5]
    }

    bear_size_hint = 0.12
    bear_size = (BasicData.window_width * bear_size_hint,
                 BasicData.window_width * bear_size_hint)


class ProductsData:
    """Константы продуктов"""
    size_hint = 0.035
    size = (BasicData.window_height * size_hint,
            BasicData.window_width * size_hint)
    life_time = 7

    # key : [name, weight, price]
    products_dict = {
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
