n = int(input('Number: '))

sum_even = 0

while n > 0:
    n = n-1

    x = int(input('> '))

    if x % 2 == 0:
        sum_even = sum_even + x

print(f'Sum of evens: {sum_even}')
