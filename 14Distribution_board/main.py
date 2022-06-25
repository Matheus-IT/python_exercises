def show_intervals(intervals: list(tuple())):
	print('Intervals:')
	for interval in intervals:
		print(f'{interval[0]:.3f} - {interval[1]:.3f}')


def show_frequency(frequency: list):
	for el in frequency:
		print(f'{el:.3f}')


def main():
	from math import sqrt
	from Calc_intervals_for_distribution_frequency_board import calc_intervals, calc_means_of_intervals
	from Calc_frequencies import calc_absolute_frequency, calc_relative_frequency
	from Calc_dispersion_measures import calc_standard_deviation, calc_arithmetic_mean

	elements = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8,
9, 9, 10, 10, 10]
	
	n_of_elements = len(elements)
	
	n_of_intervals: int = 5 if n_of_elements < 25 else int(sqrt(n_of_elements))
	
	total_amplitude: float = float(max(elements) - min(elements))
	
	intervals_amplitude: float = total_amplitude / n_of_intervals
	
	print(f'N of elements {n_of_elements}')
	print(f'N of intervals {n_of_intervals}')
	print(f'Total amplitude {total_amplitude}')
	print(f'Intervals amplitude {intervals_amplitude}')
	
	intervals: list(tuple()) = calc_intervals(elements)
	show_intervals(intervals)

	absolute_frequency: list = calc_absolute_frequency(elements, intervals)
	
	print('Absolute frequency:')
	show_frequency(absolute_frequency)

	relative_frequency: list = calc_relative_frequency(absolute_frequency, n_of_elements)
	print('Relative frequency:')
	show_frequency(relative_frequency)


	means_of_intervals: list = calc_means_of_intervals(intervals)
	print(f'Means of intervals {means_of_intervals}')
	print(f'Arithmetic mean {calc_arithmetic_mean(absolute_frequency, means_of_intervals, n_of_elements)}')
	print(f'Standard deviation {calc_standard_deviation(absolute_frequency, means_of_intervals, n_of_elements)}')


if __name__ == '__main__':
	main()
