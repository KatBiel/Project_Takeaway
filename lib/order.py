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