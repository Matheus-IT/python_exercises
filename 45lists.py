from random import randint
from sympy import isprime


l1 = []

for i in range(10):
	l1.append(randint(0, 99))

print(l1)

primes = list(filter(isprime, l1))
print(primes)
