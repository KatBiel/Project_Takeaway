from lib.order import *
from unittest.mock import Mock

def test_order_initializer():
    menu = Mock()
    order = Order(menu)
    assert order.menu == menu
    assert order.order_list == []