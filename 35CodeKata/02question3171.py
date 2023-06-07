while True:
    try:
        n, l = list(map(int, input().split()))
    except EOFError:
        break

    links = [
        tuple(
            map(
                int,
                input().split(),
            )
        )
        for _ in range(l)
    ]

    print(links)
    print(n)

    if len(links) < n - 1:
        print("INCOMPLETO")
    else:
        print("COMPLETO")
