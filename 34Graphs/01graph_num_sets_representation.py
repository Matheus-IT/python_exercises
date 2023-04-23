from graph import get_edges, get_vertices


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
