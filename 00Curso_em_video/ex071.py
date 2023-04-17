print(' - '*14)
print('{:=^40}'.format('Banco Centavo Não'))
print(' - '*14)
saque = int(input('Qual valor você quer sacar? R$'))
print('='*40)
cel_50 = int(saque / 50)
if cel_50 > 0:
    print(f'Total de {cel_50} cédulas de R$50')
cel_20 = int((saque % 50) / 20)
if cel_20 > 0:
    print(f'Total de {cel_20} cédulas de R$20')
cel_10 = int(((saque % 50) % 20) / 10)
if cel_10 > 0:
    print(f'Total de {cel_10} cédulas de R$10')
moed_1 = int((((saque % 50) % 20) % 10) / 1)
if moed_1 > 0:
    print(f'Total de {moed_1} moédas de R$1')
print('='*40)
