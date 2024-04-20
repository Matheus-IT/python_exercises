size = int(input())

numbers = 0
last_value = None

for _ in range(size):
    n = int(input())

    if n != last_value:
        numbers += 1

    last_value = n

print(numbers)
