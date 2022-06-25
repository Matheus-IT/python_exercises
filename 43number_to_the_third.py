m = int(input('m: '))

# amount of digits of m
w1 = len(str(m))

# Starting odd number
odd = 1

# Generate m cube sequences

# Need to finish...
for n in range(1, m+1):
	print(f'{n:{w1}}^3 = ', end='')

	for k in range(n):
		print(odd, end='')

		if k < n-1:
			print('+', end='')
		odd += 2
	print()

# Generate m cube sequences
# for n in range(1, m+1):
# 	print(f'{n:{w}^3} = {odd}', end='')
#
# 	for k in range(1, n):
# 		print(f'+ {odd + 2*k}', end='')
# 	print()
#
# 	odd += 2*n


