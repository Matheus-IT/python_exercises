from graph import get_edges


def main():
    with open("34Graphs/in2.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))
        matrix = []
        for _ in range(qv):
            matrix.append([0 for _ in range(qv)])

        edges = get_edges(f)

        for e in edges:
            matrix[e[0] - 1][e[1] - 1] = 1
            matrix[e[1] - 1][e[0] - 1] = 1

        for l in matrix:
            print(l)


if __name__ == "__main__":
    main()
