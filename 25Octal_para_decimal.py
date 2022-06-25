num = str(input(' - Digite um numero em octal: '))
cont2 = 0
decimal = 0
for cont in range(len(num)-1, -1, -1):
    decimal += int(num[cont]) * 8**cont2
    cont2 += 1
print(decimal)
