binario = str(input(' - Digite um numero binario: '))
decimal = 0
cont2 = 0
for cont in range(len(binario)-1, -1, -1):
    decimal += (int(binario[cont]) * 2**cont2) if binario[cont] == '1' else 0
    cont2 += 1
print(f' - O numero {binario} em decimal {decimal}')
