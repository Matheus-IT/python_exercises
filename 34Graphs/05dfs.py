from queue import LifoQueue
from graph import get_edges, get_adjacency_vector


def main():
    with open("34Graphs/in3.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))

        edges = get_edges(f)

        adj_vector = get_adjacency_vector(edges, qv)

        marked = {i + 1: False for i in range(qv)}
        discovered = LifoQueue()
        explored = []

        root = int(input("Escolha qual será a raiz:"))

        discovered.put(root)

        while not discovered.empty():
            v = discovered.get()

            if not marked[v]:
                marked[v] = True
                explored.append(v)

                for neighbor in adj_vector[v][::-1]:
                    discovered.put(neighbor)
        print(explored)


if __name__ == "__main__":
    main()
