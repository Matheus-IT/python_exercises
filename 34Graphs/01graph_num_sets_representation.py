def get_edges(f):
    return [tuple(line.strip().split(" ")) for line in f.readlines()]


def get_vertices_labels(a):
    flattened = []
    list(flattened.extend(item) for item in a)
    flattened = set(flattened)
    return sorted(flattened)


def show_graph(g):
    print("G(V,E):")
    print("V =", g["V"])
    print("E =", g["E"])


def main():
    with open("34Graphs/in1.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))

        graph = dict()
        graph["E"] = get_edges(f)
        graph["V"] = get_vertices_labels(graph["E"])

        show_graph(graph)


if __name__ == "__main__":
    main()
