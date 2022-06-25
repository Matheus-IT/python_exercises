class Vehicle:
    def __init__(self, name, max_speed, mileage=0):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'The vehicle {self.name} has {capacity} seats'


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f'The bus {self.name} has {capacity} seats'


class Car(Vehicle):
    pass


def main():
    v1 = Vehicle('uno', 180)
    v2 = Vehicle('vectra', 220, 15000)

    b1 = Bus('w8', 180, 15)
    b2 = Bus('volare', 180)

    print(v1.seating_capacity(5))
    print(v2.seating_capacity(5))
    print(b1.seating_capacity(35))
    print(b2.seating_capacity(45))


if __name__ == '__main__':
    main()
