from twilio.rest import Client
from datetime import datetime, timedelta

class Order():
    def __init__(self, menu, twilio_serive=None):
        self.menu = menu
        self.order_list = []
        self.twilio_service = twilio_serive

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


    def all_selected(self):
        return self.order_list

    def generate_receipt(self, customer_phone=None):
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
        receipt = f'{joined_receipt_lines}{total_line}'
        
        if self.twilio_service and customer_phone:
            self.twilio_service.send_confirmation(customer_phone)

        return receipt
        
        
        
