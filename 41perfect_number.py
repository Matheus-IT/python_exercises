def is_divisible(n1: int, n2: int):
	return n1 % n2 == 0


n = int(input('Enter a number: '))

sum_divisors = 0

for i in range(1, n):
	if is_divisible(n, i):
		sum_divisors += i

print(f'Sum of divisors of {n} is equal to {sum_divisors}')

print(f'the number {n} is ', end='')

if sum_divisors < n:
	print('deficient')
elif sum_divisors > n:
	print('abundant')
else:
	print('perfect')
