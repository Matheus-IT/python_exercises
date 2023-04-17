def main():
    with open("34Graphs/in1.txt") as f:
        qv, qa = map(int, f.readline().split(" "))
        a = []

        for line in f.readlines():
            print(line)
            line = line.replace("\n", "")
            a.append(tuple(line.split(" ")))

        print("a", a)


if __name__ == "__main__":
    main()
