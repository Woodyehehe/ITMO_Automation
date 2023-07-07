class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print('Автомобиль заведен')

    def stop_car(self):
        print('Автомобиль заглушен')

    def year_car(self):
        print(self.year)

    def type_car(self):
       print(self.type)

    def color_car(self):
        print(self.color)

car1 = Car('Черный', 'Бешеная табуретка', 2007)
car1.start_car()
car1.stop_car()
car1.year_car()
car1.type_car()
car1.color_car()


