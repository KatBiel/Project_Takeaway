class Order():
    def __init__(self, menu):
        self.menu = menu
        self.order_list = []

    def add(self, dish, quantity):
        dish_name = dish.name
        item_found = False
        for menu_dish in self.menu.dishes:
            if menu_dish.name == dish_name:
                item_found = True
            else: 
                raise Exception(f"Dish not available")

        # self.order_list.append((dish, quantity))
        price = float(dish.price)
        self.order_list.append({'dish': dish, 'quantity': quantity, 'price': price * quantity} )


        # Consider adding validation to check whether the provided dish name exists in the menu before adding it to the order.
        #Raises: ValueError if the provided dish name does not exist in the menu.

    def all_selected(self):
        return self.order_list

    def generate_receipt(self):
        #returns:
        # a dictionary with keys 'order_details' (list of selected dishes with details)
        # and 'total' (grand total price).
        pass