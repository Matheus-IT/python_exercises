from graph import get_edges, get_adjacency_vector

with open("34Graphs/in4.txt") as f:
    qv, qe = map(int, f.readline().strip().split(" "))

    edges = get_edges(f)

    adj_vec = get_adjacency_vector(edges, qv, is_directed=True)
