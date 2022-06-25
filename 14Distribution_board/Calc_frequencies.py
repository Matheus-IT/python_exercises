def how_many_in_the_open_interval(elements: list, interval: tuple()) -> int:
	count = 0
	for el in elements:
		if interval[0] <= el < interval[1]:
			count += 1
	return count


def how_many_in_the_closed_interval(elements: list, interval: tuple()) -> int:
	count = 0
	for el in elements:
		if interval[0] <= el <= interval[1]:
			count += 1
	return count


def calc_absolute_frequency(elements: list, intervals: list(tuple())) -> list:
	absolute_frequency = []
	for i in range(len(intervals)):
		if i == len(intervals) - 1:
			absolute_frequency.append(how_many_in_the_closed_interval(elements, intervals[i]))
			break
		absolute_frequency.append(how_many_in_the_open_interval(elements, intervals[i]))
	return absolute_frequency


def calc_relative_frequency(absolute_frequency: list, n_of_elements: int) -> list:
	relative_frequency = []
	for el in absolute_frequency:
		relative_frequency.append(el / n_of_elements)
	return relative_frequency
