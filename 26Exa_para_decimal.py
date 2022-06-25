num = str(input(' - Digite um numero em exadecimal: '))
decimal = 0
cont2 = 0
for cont in range(len(num)-1, -1, -1):
    if (num[cont].upper() == 'A'):
        decimal += 10 * 16**cont2
    elif (num[cont].upper() == 'B'):
        decimal += 11 * 16**cont2
    elif (num[cont].upper() == 'C'):
        decimal += 12 * 16**cont2
    elif (num[cont].upper() == 'D'):
        decimal += 13 * 16**cont2
    elif (num[cont].upper() == 'E'):
        decimal += 14 * 16**cont2
    elif (num[cont].upper() == 'F'):
        decimal += 15 * 16**cont2
    else:
        decimal += int(num[cont]) * 16**cont2
    cont2 += 1
print(f' - Decimal {decimal}')
