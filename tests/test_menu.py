from lib.menu import *

def test_initially_empty_list():
    menu = Menu()
    assert menu.list_all_dishes() == []