from libs.libs import *
from src.Map.Field import PlayingField
from src.Data.Constants import BasicData, AnimalData
from src.Map.Money import Money
import src.Map.Places.PlacesImports as Places

Builder.load_file("kv/Map/Map.kv")


class Map(FloatLayout):
    """
        Класс Игры
    Поля:
        events: События, которые постоянно происходят на карте
        is_stopped: Показывает приостановлены ли события
    """
    events = list()
    is_stopped = False

    def __init__(self, **kwargs):
        """
            Создаёт игру:
          1)Задает начальную сумму денег
          2)Устанавливает имена некоторых виджетов на карте
          3)Запускает постоянно повторяющиеся события
        """
        super(Map, self).__init__(**kwargs)
        Money.assign(BasicData.starting_amount_of_money)
        self.money_label.text = str(Money.get_money())
        self.set_names()
        self.game_start()

    def set_names(self):
        """Устанавливает надписи на кнопках покупки животных, фабриках и складе"""
        self.animal_button1.text = "    " + str(AnimalData.animal_dict["chicken"][2]) + \
                                   "\n" + AnimalData.animal_dict["chicken"][0]
        self.animal_button2.text = " " + str(AnimalData.animal_dict["goat"][2]) + "\n" + \
                                   AnimalData.animal_dict["goat"][0]
        self.animal_button3.text = str(AnimalData.animal_dict["cow"][2]) + "\n  " + AnimalData.animal_dict["cow"][0]
        self.animal_button4.text = str(AnimalData.animal_dict["pig"][2]) + "\n   " + AnimalData.animal_dict["pig"][0]

        self.flour_creator.create_button.text = "flour"
        self.oil_creator.create_button.text = "goat oil"
        self.cheese_creator.create_button.text = "cheese"
        self.cutting_creator.create_button.text = "truffle cutting"

        self.storage.storage_button.text = "0 / " + str(self.storage.capacity)

    def game_start(self):
        """Метод, запускающий постоянно повторяющиеся события"""
        self.is_stopped = False
        self.events.append(Clock.schedule_interval(self.field.animal_movement, 1 / BasicData.FPS))
        self.events.append(Clock.schedule_interval(self.field.product_disappearing, 1 / BasicData.FPS))

    def game_stop(self):
        """Метод, приостанавливающий постоянно повторяющиеся события"""
        self.is_stopped = True
        for event in self.events:
            Clock.unschedule(event)

    def update_money(self, delta):
        """Изменяет сумму денег"""
        Money.change_money(delta)
        self.money_label.text = str(Money.get_money())
