n, l = list(map(int, input().split()))

segments = [i + 1 for i in range(n)]

links = [
    tuple(
        map(
            int,
            input().split(),
        )
    )
    for _ in range(l)
]


temp = links.copy()
hanging = []

for link in links:
    temp.remove(link)
    hanging_left = [l[0] for l in temp]
    hanging_right = [l[1] for l in temp]

    if (
        link[0] in hanging_left
        or link[0] in hanging_right
        or link[1] in hanging_left
        or link[1] in hanging_right
    ):
        temp.append(link)
        continue
    hanging.append(link)

if hanging:
    print("INCOMPLETO")
else:
    print("COMPLETO")
