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


def verify(link, temp):
    for l in temp:
        if link[0] == l[0] or link[0] == l[1] or link[1] == l[0] or link[1] == l[1]:
            temp.append(link)
            return True
    return False


for link in links:
    temp.remove(link)

    if not verify(link, temp):
        continue
    hanging.append(link)

if hanging:
    print("INCOMPLETO")
else:
    print("COMPLETO")
