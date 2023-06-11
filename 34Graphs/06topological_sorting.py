from graph import get_edges, get_adjacency_vector
from queue import LifoQueue


def topological_sorting(adj_vec):
    order = []
    de = [0] * len(adj_vec)

    for e in adj_vec.values():
        for w in e:
            de[w - 1] += 1

    degree_zero = LifoQueue()
    for i, degree in enumerate(de):
        if degree == 0:
            degree_zero.put(i + 1)

    while not degree_zero.empty():
        v = degree_zero.get()
        order.append(v)

        for w in adj_vec[v]:
            de[w - 1] -= 1

            if de[w - 1] == 0:
                degree_zero.put(w)
    return order


with open("34Graphs/in4.txt") as f:
    qv, qe = map(int, f.readline().strip().split(" "))

    edges = get_edges(f)
    adj_vec = get_adjacency_vector(edges, qv, is_directed=True)

    order = topological_sorting(adj_vec)
    print(order)
