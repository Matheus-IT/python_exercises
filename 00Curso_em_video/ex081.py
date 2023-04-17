v = []
pos_5 = []
tot_num = 0
while True:
    v.append(int(input('Digite um valor: ')))
    tot_num += 1 #Acumular total de números
    resp = str(input('Quer mais um número? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('\033[1;31mOpção inválida!\033[m Quer mais um número? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

if 5 in v:
    for c, val in enumerate(v): #Posições do 5 na lista de valores
        if val == 5:
            pos_5.append(c)
v.sort(reverse=True)
print('-=-'*10)
print(f'Foram digitados um total de {tot_num} números')
print('-=-'*10)
print('Lista de valores em ordem decrescente')
print('-=-'*5)
for val in v:
    print(f'|{val}|')
print('-=-'*5)
if len(pos_5) == 0: #Se não tiver nenhum 5
    print('O valor 5 não foi digitado')
else:
    print('O valor 5 foi digitado na(s) posição(ões): ', end='')
for val in pos_5:
    print(val, end=' ')
