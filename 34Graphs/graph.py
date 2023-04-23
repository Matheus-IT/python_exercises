def get_edges(f):
    return [
        tuple(
            map(int, line.strip().split(" ")),
        )
        for line in f.readlines()
    ]


def get_vertices(num_vertices):
    return [i for i in range(1, num_vertices + 1)]
