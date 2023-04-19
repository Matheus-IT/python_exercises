def get_edges(f):
    return [
        tuple(
            map(int, line.strip().split(" ")),
        )
        for line in f.readlines()
    ]


def get_vertices(num_vertices):
    return [i for i in range(1, num_vertices + 1)]


def show_graph(g):
    print("G(V,E):")
    print("V =", g["V"])
    print("E =", g["E"])


def main():
    with open("34Graphs/in2.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))

        graph = dict()
        graph["E"] = get_edges(f)
        graph["V"] = get_vertices(qv)

        show_graph(graph)


if __name__ == "__main__":
    main()
