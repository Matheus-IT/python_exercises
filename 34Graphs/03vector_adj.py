from graph import get_edges, get_adjacency_vector


def main():
    with open("34Graphs/in2.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))

        edges = get_edges(f)

        adj_vector = get_adjacency_vector(edges, qv)

        for k, v in adj_vector.items():
            print(k, v)


if __name__ == "__main__":
    main()
