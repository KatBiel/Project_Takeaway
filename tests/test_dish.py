from lib.dish import *

def test_initializer():
    dish = Dish('Pizza', '12.50')
    assert dish.name == 'Pizza'
    assert dish.price == '12.50'