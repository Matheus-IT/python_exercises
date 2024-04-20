from calendar import monthrange

m = int(input('Month: '))
y = int(input('Year: '))

f, n = monthrange(y, m)

print(' S  T  Q  Q  S  S  D')
print('         ')

for d in range(1, n+1):
	print(f'{d:2} ', end='')
	f += 1

	if f > 6:
		f = 0
		print()
print()
