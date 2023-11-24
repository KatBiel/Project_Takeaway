class Order():
    def __init__(self, menu):
        self.menu = menu
        self.order_list = []

    def add(self, dish, quantity):
        price = float(dish.price)
        item_found = False
        for item in self.menu.dishes:
            if item.name == dish.name:
                item_found = True
                break

        if not item_found:
            raise Exception("Dish not available")
            
        self.order_list.append({'dish': dish, 'quantity': quantity, 'price': price * quantity} )
        # self.order_list.append((dish, quantity))


    def all_selected(self):
        return self.order_list

    def generate_receipt(self):
        #returns:
        # a dictionary with keys 'order_details' (list of selected dishes with details)
        # and 'total' (grand total price).
        pass