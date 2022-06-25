while True:
    print('Número negativo para sair')
    num = int(input('Ver tabuada de qual número? '))
    if num < 0: #Se for um número negativo, parar
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-='*15)
print('Calculadora finalizada. Volte sempre!')
