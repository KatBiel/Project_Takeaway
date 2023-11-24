# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

>Use the twilio-python package to implement this next one. You will need to use mocks too:

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

* Nouns:
menu
order
list of dishes
prices
text confirmation


* Verbs:
add dishes
select number of dishes
verify correct order: see receipt with grand total
text confirmation

```

```

_Also design the interface of each class in more detail._

```python
class Menu:
    # User-facing properties:
    #   dishes: list of instances of Dishes

    def __init__(self):
        # side effect: initialises an empty list
        # returns: nothing
        # self.dishes = []
        pass 

    def add(self, dish):
        # Parameters:
        #   dish: an instance of Dish
        # Side-effects:
        #   Adds the dish to the dishes property of the self object
        # Returns nothing
        pass 

    def list_all_dishes(self):
        # Returns:
        #   A list of the Dishes instances
        pass 


class Dish():
    # User-facin (Public) properties:
    #   name: string representing a name of a dish
    #   price: a float representing the price of a dish

    def __init__(self, name, price):
        # Parameters:
        #   name: string
        #   price: float
        # Side-effects:
        #   Sets the above (name and price) properties
        pass 

class Order():
    def __init__(self, menu):
        # side effect: initialises an empty list
        # menu: a string, an instance of Menu
        # returns: nothing
        # self.menu = menu
        # self.order_list = []
        pass

    def add(self, dish, quantity):
        # dish: string, an instance of Dish, 
        #    representing a dish name selected by the user
        # quantity: int representing a number of dishes selected
        # Consider adding validation to check whether the provided dish name exists in the menu before adding it to the order.
        #Raises: ValueError if the provided dish name does not exist in the menu.
        pass

    def all_selected(self):
        #returns: A list of dictionaries with keys 'dish_name', 'quantity', and 'price'.
        pass

    def generate_receipt(self):
        #returns:
        # a dictionary with keys 'order_details' (list of selected dishes with details)
        # and 'total' (grand total price).
        pass

# {
#     'order_details': [
#         {'dish_name': 'Pizza'', 'quantity': 1, 'price': 12.50},
#         {'dish_name': 'Lasagne', 'quantity': 2, 'price': 21.80}
#     ],
#     'total': £34.30
# }

class TwilioService():
    def __init__(self):
        pass

    def send_text_confirmation(self, phone_number, delivery_time):
        #returns a string function:
        #   f"Thank you! Your order was placed and will be delivered before {delivery_time}"
        pass



```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE



"""
class Menu: When we add multiple dishes entries, list_of_all_dishes lists them out
"""
def test_list_of_all_dishes():
    menu = Menu()
    dish_1 = Dish('Pizza' '12.50')
    dish_2 = Dish('Lasagne' '10.90')
    dish_3 = Dish('Spaghetti' '9.50')
    menu.dishes.add(dish_1)
    menu.dishes.add(dish_2)
    smenu.dishes.add(dish_2)
    assert menu.list_all_dishes() == [dish_1, dish_2, dish_3]

"""
class Order: Test initialiser for Order class
"""
def test_order_initializer():
    menu = Menu() 
    order = Order(menu)
    assert order.menu == menu
    assert order.order_list == []


"""
class Order: When added multiple dishes to order list, all_selected() returns list of dictionaries with keys 'dish_name', 'quantity', and 'price'.
"""
def test_order_list():
    order = Order()
    dish_1 = Dish('Pizza' '12.50')
    dish_2 = Dish('Lasagne' '10.90')
    self.order_list.add(dish_1, 1)
    self.order_list.add(dish_2, 2)
    assert order.order_list() == [(dish_1, 1), (dish_2, 2)]

"""
class Order: When adding dish that does not exist, raises an error
"""
def test_add_non_existing_dish():
    with pytest.rasises(Exception) as e:
        order.add()
    error_message = str(e.value)
    assert error_ message == 'Dish not available!'



def test_add_non_existing_dish():
    with pytest.rasises(Exception) as e:
        order.add('')
    error_message = str(e.value)
    assert error_ message == 'Empty entry!'

"""
class Order: When added multiple dishes to order list, generate_receipt() returns a dictionary
with keys 'order_details' (list of selected dishes with details)
and 'total' (grand total price).
"""
def test_generate_receipt():
    order = Order()
    dish_1 = Dish('Pizza' '12.50')
    dish_2 = Dish('Lasagne' '10.90')
    self.order_list.add(dish_1, 1)
    self.order_list.add(dish_2, 2)
    assert order.generate_receipt() == {
    'order_details': [
        {'dish_name': 'Pizza', 'quantity': '1', 'price': '12.50'},
        {'dish_name': 'Lasagne', 'quantity': '2', 'price': '21.80'}
    ],
    'total': £34.30
}
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

# class Menu:
"""
Initialy returns an empty list
"""
def test_initially_empty_list():
    menu = Menu()
    assert menu.list_all_dishes() == []

# class Dish:
"""
Test creator
"""
def test_initializer():
    dish = Dish('Pizza' '12.50')
    assert self.name == 'Pizza'
    assert self.price == '12.50'

# class Order()
"""
Initially returns an empty list
"""
def test_initially_an_empty_list():
    order = Order()
    assert order.order_list == []

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
