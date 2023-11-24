class Menu():
    # User-facing properties:
    #   dishes: list of instances of Dishes

    def __init__(self):
        self.dishes = []

    def add(self, dish):
        self.dishes.append(dish)

    def list_all_dishes(self):
        return self.dishes
