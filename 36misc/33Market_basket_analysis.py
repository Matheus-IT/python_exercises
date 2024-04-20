def calcOccurrences(itemset: list) -> int:
	return len(list(filter(lambda x: x == 1, itemset)))


def calcOccurrencesOfBoth(itemset1: list, itemset2: list) -> int:
	count: int = 0
	for i in range(len(itemset1)):
		if itemset1[i] == 1 and itemset2[i] == 1:
			count += 1
	return count


def support(*itemsets) -> float:
	occurrencesOfItem: float = 0
	if len(itemsets) == 1:
		occurrencesOfItem = calcOccurrences(itemsets[0])
	elif len(itemsets) == 2:
		occurrencesOfItem = calcOccurrencesOfBoth(itemsets[0], itemsets[1])
	return occurrencesOfItem / len(itemsets[0])


def confidence(itemset1: list, itemset2: list) -> float:
	supportOfBoth: float = support(itemset1, itemset2)
	return supportOfBoth / support(itemset1)


def lift(itemset1: list, itemset2: list):
	supportOfBoth = support(itemset1, itemset2)
	return supportOfBoth / (support(itemset1) * support(itemset2))


def main():
	basket: dict = {
		'milk':		[1, 1, 1, 0],
		'eggs': 	[1, 1, 0, 1],
		'apples': 	[0, 0, 0, 1],
		'bread': 	[1, 0, 1, 0]
	}

	print(f'Support {support(basket["milk"])}')
	print(f'Confidence {confidence(basket["milk"], basket["eggs"])}')
	print(f'Lift {lift(basket["milk"], basket["eggs"])}')


if __name__ == '__main__':
	main()
