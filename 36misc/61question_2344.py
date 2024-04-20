n = int(input())

if n == 0:
    grade = "E"
elif 1 <= n <= 35:
    grade = "D"
elif 36 <= n <= 60:
    grade = "C"
elif 61 <= n <= 85:
    grade = "B"
else:
    grade = "A"

print(grade)
