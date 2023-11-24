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
    menu.add(dish_1)
    menu.add(dish_2)
    order.add(dish_1, 1)
    order.add(dish_2, 2)
    assert order.all_selected() == [
        {'dish': dish_1, 'quantity': 1, 'price': 12.50},
        {'dish': dish_2, 'quantity': 2, 'price': 10.90}
    ]
    # assert order.all_selected() == [(dish_1, 1), (dish_2, 2)]


def test_add_non_existing_dish():
    menu = Menu()
    order = Order(menu)
    with pytest.raises(Exception) as e:
        order.add(Dish('Burger', '8.90'), 1)
    error_message = str(e.value)
    assert error_message == "Dish not available"

def test_generate_receipt():
    menu = Menu()
    order = Order(menu)
    dish_1 = Dish('Pizza', '12.50')
    dish_2 = Dish('Lasagne', '10.90')
    menu.add(dish_1)
    menu.add(dish_2)
    order.add(dish_1, 1)
    order.add(dish_2, 2)
    assert order.generate_receipt() == "Pizza: 1 x £12.50\nLasagne: 2 x £10.90\n\nGrand Total: £34.30"

'''
The order details:
Pizza: 1 x 12.50
Lasagne: 2 x 10.90

Total: (1 x 12.50 + 2 x 10.90) £ 33.40
self.order_list


'''