n = int(input())

total = 0

for _ in range(n):
    time, velocity = list(map(int, input().split(" ")))
    total += time * velocity

print(total)
