from queue import Queue
from graph import get_edges, get_adjacency_vector


def main():
    with open("34Graphs/in1.txt") as f:
        qv, qe = map(int, f.readline().strip().split(" "))

        edges = get_edges(f)

        adj_vector = get_adjacency_vector(edges, qv)
        root = 1

        unknown = [i + 1 for i in range(qv)]
        discovered = Queue()
        explored = []

        unknown.remove(root)
        discovered.put(root)

        while not discovered.empty():
            v = discovered.get()

            for neighbor in adj_vector[v]:
                if neighbor in unknown:
                    unknown.remove(neighbor)
                    discovered.put(neighbor)
            explored.append(v)

        print(explored)


if __name__ == "__main__":
    main()
