def find_most_frequent(nums: list) -> float:
	most_frequent = 0
	occurrences = {}

	for n1 in nums:
		frequencies = 0
		for n2 in nums:
			if n1 == n2:
				frequencies += 1
		if frequencies > most_frequent:
			most_frequent = n1
	return most_frequent


def main():
	nums: list(float) = [33.21, 42.13, 38.27, 41.81, 26.73, 38.69, 39.85, 40.02, 27.71, 36.54, 46.54, 44.68, 37.83, 40.50, 26.01, 47.01, 31.56, 42.77, 41.84, 12.83, 41.30, 39.70, 20.87, 42.23, 27.81, 31.85, 34.47, 30.59]

	print(f'The most frequent value is {find_most_frequent(nums)}')


if __name__ == '__main__':
	main()
