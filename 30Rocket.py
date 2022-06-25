class Rocket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('I created a rocket')

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        print('Vroooommmm')

    def print_rocket(self):
        print(f'x = {self.x} y = {self.y}')


r1 = Rocket(0, 0)
r1.move_rocket(1, 6)
r1.print_rocket()
