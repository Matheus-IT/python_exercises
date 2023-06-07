while True:
    try:
        n = int(input())
    except EOFError:
        break

    meat = []

    for i in range(n):
        name, exp_date = input().split()
        exp_date = int(exp_date)

        meat.append((name, exp_date))

    meat.sort(key=lambda x: x[1])

    for i in range(len(meat)):
        if i == len(meat) - 1:
            print(meat[i][0])
        else:
            print(meat[i][0], end=" ")
