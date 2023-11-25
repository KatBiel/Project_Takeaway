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
            
        self.order_list.append({'dish': dish, 'quantity': quantity} )
        # self.order_list.append((dish, quantity))


    def all_selected(self):
        return self.order_list

    def generate_receipt(self):
        receipt_lines = []
        for item in self.order_list:
            dish_name = item['dish'].name
            quantity = item['quantity']
            price = float(item['dish'].price)

            line = f"{dish_name}: {quantity} x £{price:.2f}"
            receipt_lines.append(line)
        joined_receipt_lines = '\n'.join(receipt_lines)

        total = 0
        for item in self.order_list:
            quantity = item['quantity']
            price = float(item['dish'].price)
            item_cost = price * quantity
            total += item_cost
        total_line = f"\n\nTotal: £{total:.2f}"
        
        return f'{joined_receipt_lines}{total_line}'
