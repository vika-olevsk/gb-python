import random

class Car:
    def __init__(self, sp, col, n, i_p):
        self.speed = sp
        self.color = col
        self.name = n
        self.is_police = i_p

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self):
        i = random.randint(0, 10)
        if i % 2 == 0:
            print('Turn right!')
        else:
            print('Turn left!')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed limit exceeded! Speed is {self.speed}')
        else:
            print(f'Speed is {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed limit exceeded! Speed is {self.speed}')
        else:
            print(f'Speed is {self.speed}')


class PoliceCar(Car):
    def car_type(self):
        if self.is_police == True:
            print('This is a police car')


c1 = TownCar(90, 'red', 'soul', False)
c1.show_speed()

c2 = SportCar(100, 'green', 'bmw', False)
c2.show_speed()

c3 = WorkCar(50, 'black', 'duster', False)
c3.show_speed()

c4 = PoliceCar(80, 'black', 'duster', True)
c4.car_type()

