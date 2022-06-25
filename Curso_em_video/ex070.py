print('-='*20)
print('{:=^40}'.format('Lojão Olho Da Cara'))
print('-='*20)
nome_mais_barato = ''
tot_compra = maior_mil = mais_barato = 0
while True:
    nome = str(input('Qual o \033[1;33mnome\033[m do produto? '))
    print(' -'*20)
    preco = float(input('Qual o \033[1;32mpreço\033[m do produto? '))
    tot_compra += preco #Acumular total da compra
    if preco > 1000:
        maior_mil += 1
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    print(' -'*20)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('\033[1;31mOpção inválida!\033[m Quer continuar? [S/N] ')).strip().upper()[0]
    print(' -'*20)
    if resp == 'N':
        break
print(f'''
O total da compra deu R${tot_compra:.2f}
Produtos custam mais de R$1000 foram: {maior_mil}
O mais barato foi {nome_mais_barato} que custa R${mais_barato:.2f}
''')
