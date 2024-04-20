import random
from icecream import ic


def initialize_population(population_size, x_range, y_range):
    population = []
    for _ in range(population_size):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        chromosome = (x, y)
        individual = {"chromosome": chromosome}
        population.append(individual)
    return population


def goldstein_price_function(x, y):
    term1 = 1 + ((x + y + 1) ** 2) * (
        19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2
    )
    term2 = 30 + ((2 * x - 3 * y) ** 2) * (
        18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2
    )
    return term1 * term2


def evaluate_fitness(population):
    for individual in population:
        x, y = individual["chromosome"]
        fitness = goldstein_price_function(x, y)
        individual["fitness"] = fitness
    return population


# Exemplo de uso
population_size = 50

# intervalos comummente usados para x e y
x_range = (-2, 2)
y_range = (-2, 2)

population = initialize_population(population_size, x_range, y_range)
ic(population)

print("-" * 50)

population = evaluate_fitness(population)
ic(population)
