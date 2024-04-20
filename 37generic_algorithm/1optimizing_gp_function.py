import random
from icecream import ic


def initialize_population(population_size, x_range, y_range):
    population = []
    for _ in range(population_size):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        chromosome = (x, y)
        population.append(chromosome)
    return population


# Exemplo de uso
population_size = 50
x_range = (-2, 2)  # Intervalo válido para x
y_range = (-2, 2)  # Intervalo válido para y

population = initialize_population(population_size, x_range, y_range)
ic(population)
