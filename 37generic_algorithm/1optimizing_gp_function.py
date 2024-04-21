import random


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
    global times_calculated_fitness

    for individual in population:
        x, y = individual["chromosome"]
        fitness = goldstein_price_function(x, y)
        individual["fitness"] = fitness
        times_calculated_fitness += 1
    return population


def tournament_selection(population, tournament_size):
    # Seleciona aleatoriamente k cromossomos para o torneio
    tournament_candidates = random.sample(population, tournament_size)
    # Escolhe o cromossomo com a menor aptidão no torneio
    parent1 = min(tournament_candidates, key=lambda e: e["fitness"])

    # Seleciona aleatoriamente k cromossomos para o torneio
    tournament_candidates = random.sample(population, tournament_size)
    # Escolhe o cromossomo com a menor aptidão no torneio
    parent2 = min(tournament_candidates, key=lambda e: e["fitness"])

    return parent1, parent2


def crossover(parent1, parent2):
    # Realiza o cruzamento
    child1 = {"chromosome": (parent1["chromosome"][0], parent2["chromosome"][1])}
    child2 = {"chromosome": (parent2["chromosome"][0], parent1["chromosome"][1])}

    return child1, child2


def mutate(individual, x_range, y_range):
    chromosome = individual["chromosome"]
    i = random.randint(0, 1)
    if i == 0:
        chromosome = (random.uniform(x_range[0], x_range[1]), chromosome[1])
    else:
        chromosome = (chromosome[0], random.uniform(y_range[1], y_range[1]))
    individual["chromosome"] = chromosome
    return individual


def replacement(population, new_population):
    combined_population = population + new_population

    # Ordena os cromossomos combinados com base na aptidão
    combined_population_sorted = sorted(combined_population, key=lambda x: x["fitness"])

    # Seleciona os melhores cromossomos para a próxima geração
    next_generation = combined_population_sorted[: len(population)]

    return next_generation


algorithm_executions = 100
times_calculated_fitness = 0
optimal_fitness = 3
minimal_rate_to_hit = 0.01
hits = 0


for _ in range(algorithm_executions):
    population_size = 50
    generation = 1

    # intervalos comummente usados para x e y
    x_range = (-2, 2)
    y_range = (-2, 2)

    population = initialize_population(population_size, x_range, y_range)
    population = evaluate_fitness(population)

    history_of_best = []

    while True:
        children = []

        for _ in range(len(population) // 2):
            parent1, parent2 = tournament_selection(population, tournament_size=3)
            child1, child2 = crossover(parent1, parent2)

            children.append(child1)
            children.append(child2)

        mutation_rate = 0.1

        for individual in children:
            if random.random() < mutation_rate:
                individual = mutate(individual, x_range, y_range)

        children = evaluate_fitness(children)

        population = replacement(population, children)

        generation += 1

        best = min(population, key=lambda x: x["fitness"])
        history_of_best.append(best)

        # mantém histórico de melhores com 5 elementos no máximo
        if len(history_of_best) == 6:
            history_of_best.pop(0)

        # se o melhor não melhorou nas últimas 3 vezes chegou a hora de parar
        if len(history_of_best) == 5 and all(
            history_of_best[0]["fitness"] == e["fitness"] for e in history_of_best
        ):
            print(best)

            if (best["fitness"] - optimal_fitness) < minimal_rate_to_hit:
                hits += 1

            break

print(f"Acertos {hits}")
