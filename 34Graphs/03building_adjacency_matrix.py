def get_edges(f):
    a = []
    for line in f.readlines():
        print(line)
        line = line.replace("\n", "")
        a.append(tuple(line.split(" ")))
    return a


def get_vertices_labels(a):
    flattened = []
    list(flattened.extend(item) for item in a)
    flattened = set(flattened)
    return sorted(flattened)


def main():
    with open("34Graphs/in1.txt") as f:
        qv, qa = map(int, f.readline().split(" "))
        a = get_edges(f)

        print("a", a)
        v = get_vertices_labels(a)

        print("v", v)


if __name__ == "__main__":
    main()
