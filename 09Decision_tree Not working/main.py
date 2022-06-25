

def info(field: dict) -> float:
	from math import log2

	max_instances: int = 16 # the maximum instances of the table
	r: float = 0

	for k, v in field.items():
		n1: int = v[0]
		n2: int = v[1]

		d: int = n1 + n2
		if n1 != 0 and n2 != 0:
			try:
				r += (d / max_instances) * (-(n1 / d) * log2(n1 / d) - (n2 / d) * log2(n2 / d))  # total weight
			except Exception as error:
				print(error)
	return r


def main():
	# what's the most important attribute?
	# time:
	# 	morning: f=2 n=0
	# 	afternoon: f=7 n=4
	# 	night: f=2 n=1
	# match type:
	# 	master: f=3 n=3
	# 	grand slam: f=6 n=1
	# 	friendly: f=2 n=1
	# court surface:
	# 	grass: f=4 n=0
	# 	clay: f=2 n=3
	# 	hard: f=4 n=0
	# 	mixed: f=0 n=2
	# best effort:
	# 	1: f=9 n=4
	# 	0: f=1 n=1
	# outcome: f=11, n=5

	info_g: float = info({'f,n': [11, 5]}) # general

	time: dict = {
		'morning': [2, 0],
		'afternoon': [7, 4],
		'night': [2, 1]
	}
	match_type: dict = {
		'master': [3, 3],
		'grand slam': [6, 1],
		'friendly': [2, 1]
	}
	court_surface: dict = {
		'grass': [4, 0],
		'clay': [2, 3],
		'hard': [4, 0],
		'mixed': [0, 2]
	}
	best_effort: dict = {
		'1': [9, 4],
		'0': [1, 1]
	}

	info_time: float = info(time)
	info_match_type: float = info(match_type)
	info_court_surface: float = info(court_surface)
	info_best_effort: float = info(best_effort)

	infos: list = [
		info_time,
		info_match_type,
		info_court_surface,
		info_best_effort
	]
	gains: list = []

	print('Infos: ')
	for i in infos:
		print(f'info {i:.2f}')
	print('Gains: ')
	for i in infos:
		gains.append(info_g - i)
		print(f'{info_g - i:.2f}')
	print(f'The best is {max(gains):.2f}') # root node


if __name__ == '__main__':
	main()
