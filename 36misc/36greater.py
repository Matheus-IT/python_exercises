from typing import Union


def greater(n1:int, n2:int) -> Union(int, None):
    return n1 if n1 > n2 else n2 if n2 > n1 else None


n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))

print(greater(n1, n2))
