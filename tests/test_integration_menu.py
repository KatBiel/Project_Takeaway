from lib.menu import *
from lib.dish import *

def test_list_of_all_dishes():
    menu = Menu()
    dish_1 = Dish('Pizza' '12.50')
    dish_2 = Dish('Lasagne' '10.90')
    dish_3 = Dish('Spaghetti' '9.50')
    menu.dishes.add(dish_1)
    menu.dishes.add(dish_2)
    menu.dishes.add(dish_2)
    assert menu.list_all_dishes() == [dish_1, dish_2, dish_3]