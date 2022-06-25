def calc_intervals(elements: list):
	from math import sqrt

	n_of_elements = len(elements)
	n_of_intervals: int = 5 if n_of_elements < 25 else int(sqrt(n_of_elements))

	total_amplitude: float = float(max(elements) - min(elements))
	intervals_amplitude: float = total_amplitude / n_of_intervals

	intervals: list(tuple()) = []
	n = min(elements)
	for i in range(n_of_intervals):
		intervals.append((n, n + intervals_amplitude))
		n+= intervals_amplitude
	return intervals


def calc_means_of_intervals(intervals: list(tuple())) -> list:
	means = []
	for interval in intervals:
		means.append(sum(interval) / len(interval))
	return means
