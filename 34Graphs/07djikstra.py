with open("34Graphs/in5.txt") as f:
    first_line = f.readline()
    n = int(first_line.strip().split()[0])
    m = first_line.strip().split()[1]

    adj_list = {v: [] for v in range(n)}

    for line in f:
        u = int(line.strip().split()[0])
        v = int(line.strip().split()[1])
        p = int(line.strip().split()[2])

        adj_list[u].append((v, p))

    print(adj_list)
