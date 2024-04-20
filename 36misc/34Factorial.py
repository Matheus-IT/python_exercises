def calcFactorial(n: int) -> int:
	if n == 1:
		return 1
	return n * calcFactorial(n - 1)


n = 10
print(f'Factorial of {n} is {calcFactorial(n)}')
