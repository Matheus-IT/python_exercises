class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.x}, {self.y})'


class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        # Top-left corner
        self.x1 = p1.x
        self.y1 = p1.y
        # Top-bottom corner
        self.x2 = p2.x
        self.y2 = p2.y

    def is_meteor_inside(self, p: Point):
        return self.x1 <= p.x <= self.x2 and \
               self.y2 <= p.y <= self.y1

    def __repr__(self):
        return f'[({self.x1},{self.y1}),\
                  ({self.x2},{self.y2})]'


def main():
    c = 0
    while True:
        line = input()
        data = tuple(map(int, line.split()))
        if not any(data):
            break

        p1 = Point(data[0], data[1])
        p2 = Point(data[2], data[3])
        farm = Rectangle(p1, p2)

        n = int(input())

        fall = 0

        for k in range(n):
            x, y = tuple(map(int, input().split()))
            p = Point(x, y)

            if farm.is_meteor_inside(p):
                fall += 1

        c += 1
        print(f'Teste {c}')
        print(fall)
        print()


if __name__ == '__main__':
    main()
