def calc_arithmetic_mean(absolute_frequency: list, means_of_intervals: list, total: int):
	summing = 0
	for i in range(len(absolute_frequency)):
		summing += absolute_frequency[i] * means_of_intervals[i]
	return summing / total


def calc_standard_deviation(absolute_frequency: list, means_of_intervals: list, total: int) -> float:
	from math import sqrt

	total_mean = calc_arithmetic_mean(absolute_frequency, means_of_intervals, total)
	summing = 0
	for i in range(len(absolute_frequency)):
		summing += absolute_frequency[i] * (means_of_intervals[i] - total_mean)**2
	return sqrt(summing / total)
