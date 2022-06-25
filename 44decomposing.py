n = int(input('Enter an integer number: '))

n_len = len(str(n))

while n > 1:
	i = 2

	while n % i != 0:
		i += 1

	print(f'{n:{n_len}}|{i}')
	n //= i

print(f'{n:{n_len}}|')
