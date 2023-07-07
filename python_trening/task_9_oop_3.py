class Soda:
    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}')
        else:
            print("Обычная газировка")

drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()
