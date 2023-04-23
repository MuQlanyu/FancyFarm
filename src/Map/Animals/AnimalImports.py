"""Файл для импортирования всех животных"""
from src.Map.Animals.Bear import Bear
from src.Map.Animals.Chicken import Chicken
from src.Map.Animals.Goat import Goat
from src.Map.Animals.Cow import Cow
from src.Map.Animals.Pig import Pig

# Словарь для создания животных по их названию
animal_dict = {
    "chicken": Chicken,
    "goat": Goat,
    "cow": Cow,
    "pig": Pig
}
