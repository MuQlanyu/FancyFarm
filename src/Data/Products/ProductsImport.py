"""Файл для импортирования всех продуктов"""
from src.Data.Constants import ProductsData

from src.Data.Products.Natural.Bearina import Bearina
from src.Data.Products.Natural.Egg import Egg
from src.Data.Products.Natural.GoatMilk import GoatMilk
from src.Data.Products.Natural.Milk import Milk
from src.Data.Products.Natural.Truffle import Truffle

from src.Data.Products.ManMade.Flour import Flour
from src.Data.Products.ManMade.GoatOil import GoatOil
from src.Data.Products.ManMade.Cheese import Cheese
from src.Data.Products.ManMade.TruffleCutting import TruffleCutting

# Словарь для создания продуктов по названию
product_dict = {
    "bearina": Bearina,
    "egg": Egg,
    "goat milk": GoatMilk,
    "milk": Milk,
    "truffle": Truffle,
    "flour": Flour,
    "goat oil": GoatOil,
    "cheese": Cheese,
    "truffle сutting": TruffleCutting
}
