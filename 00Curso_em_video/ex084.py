pessoas = list()
tot_pesados = list()
tot_leves = list()
mais_pesado = mais_leve = 0

while True:
    pessoas.append(str(input('Nome: ')).title().strip())
    pessoas.append(float(input('Peso: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

for c, p in enumerate(pessoas):
    if c % 2 == 1: #Varrer pessoas em seus pesos
        if c == 1: #O primeiro será o mais leve e também o mais pesado
            mais_leve = p
            mais_pesado = p
        elif p > mais_pesado: #Descobrir qual é o mais pesado
            mais_pesado = p
        elif p < mais_leve: #Descobrir qual é o mais leve
            mais_leve = p

for c, p in enumerate(pessoas):
    if p == mais_pesado:
        tot_pesados.append(pessoas[c - 1]) #O nome dos mais pesados
    elif p == mais_leve:
        tot_leves.append(pessoas[c - 1]) #O nome dos mais leves

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O nome do(s) mais pesado é {tot_pesados} e o(s) mais leve(s) é {tot_leves}.')
