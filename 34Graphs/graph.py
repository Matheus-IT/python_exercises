def get_edges(f):
    return [
        tuple(
            map(int, line.strip().split(" ")),
        )
        for line in f.readlines()
    ]


def get_vertices(num_vertices):
    return [i for i in range(1, num_vertices + 1)]


def get_adjacency_vector(edges, quantity_of_vertices, is_directed=False):
    adj_vector = {i + 1: [] for i in range(quantity_of_vertices)}

    for e in edges:
        print("e", e)
        adj_vector[e[0]].append(e[1])
        if not is_directed:
            adj_vector[e[1]].append(e[0])
    return adj_vector
