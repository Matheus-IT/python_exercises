pessoas = list()
p = dict()
sIdade = mIdade = 0

while True:
    p['nome'] = str(input('Nome: ')).title().strip()

    p['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while p['sexo'] not in 'MF': #Tratamento de limites
        p['sexo'] = str(input('\033[1;31mOpção errada!\033[m Sexo [M/F]: ')).upper().strip()[0]

    p['idade'] = int(input('Idade: '))
    sIdade += p['idade'] #Soma de todas as idades
    pessoas.append(p.copy())
    p.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN': #Tratamento de limites
        resp = str(input('\033[1;31mOpção errada!\033[m Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-='*30)
print(f'A) - Ao todo temos {len(pessoas)} pessoas cadastradas')
mIdade = sIdade/len(pessoas) #Calcular a média de idade
print(f'B) - A média de idade é de {mIdade:.2f} anos')
print(f'C) - As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end='')
print()
print(f'D) - Lista de pessoas que estão acima da média:')
for pessoa in pessoas: #Procurar em cada pessoa de 'pessoas'
    if pessoa['idade'] > mIdade:
        print(f'       * {pessoa["nome"]} que tem {pessoa["idade"]} anos')
print('-='*30)
