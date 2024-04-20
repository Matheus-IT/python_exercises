def is_prime(n:int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# n = int(input('Enter a number: '))
n = 5

print(f'Is {n} prime? {is_prime(n)}')
