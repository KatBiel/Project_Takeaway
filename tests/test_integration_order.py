from lib.order import *
from lib.menu import *
from lib.dish import *
import pytest

def test_order_initializer():
    menu = Menu() 
    order = Order(menu)
    assert order.menu == menu
    assert order.order_list == []

def test_order_list():
    menu = Menu()
    order = Order(menu)
    dish_1 = Dish('Pizza', '12.50')
    dish_2 = Dish('Lasagne', '10.90')
    order.add(dish_1, 1)
    order.add(dish_2, 2)
    # assert order.all_selected() == [(dish_1, 1), (dish_2, 2)]
    assert order.all_selected() == [
        {'dish': dish_1, 'quantity': 1, 'price': 12.50},
        {'dish': dish_2, 'quantity': 2, 'price': 21.80}
    ]
    #[{dish_1: 1, dish_2: 2}]


    def test_add_non_existing_dish():
        with pytest.rasises(Exception) as e:
            order.add()
        error_message = str(e.value)
        assert error_message == "Dish not available!D"



# def test_add_empty_entry():
#     with pytest.rasises(Exception) as e:
#         order.add('')
#     error_message = str(e.value)
#     assert error_ message == 'Empty entry!'