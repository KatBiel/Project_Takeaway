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
            
        self.order_list.append({'dish': dish, 'quantity': quantity, 'price': price } )
        # self.order_list.append((dish, quantity))


    def all_selected(self):
        return self.order_list

    def generate_receipt(self):
        receipt = "\n".join([f"{item['dish'].name}: {item['quantity']} x £{float(item['dish'].price):.2f}"
                            for item in self.order_list])
        total = sum(float(item['dish'].price) * item['quantity'] for item in self.order_list)
        receipt += f"\n\nGrand Total: £{total:.2f}"
        return receipt