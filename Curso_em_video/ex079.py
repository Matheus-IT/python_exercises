valores = []
val = 0
while True:
    val = int(input('Digite um valor: '))
    if val not in valores: #Se valores ainda não tiver val adicionar val a valores
        valores.append(val)
        print('\033[1;34mNúmero registrado com sucesso!\033[m')
    else:
        print('\033[1;33mEu já tenho esse valor. Não adicionei.\033[m')

    resp = str(input('Mais números? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('\033[1;31mResposta incorreta!\033[m Mais números? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print()
print('-=-'*15)
valores.sort() #Organizar os números em órdem crescente
print('\033[1;35mVocê digitou os valores: ', end='')
for c, v in enumerate(valores):
    print(v, end=', ' if c < len(valores) - 1 else '.\033[m') #Mostrar VÍRGULA enquanto não for o último valor, quando for mostre PONTO
