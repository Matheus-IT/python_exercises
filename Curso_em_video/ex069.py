maior_idade = tot_homens = mulheres_menor_20 = 0
while True:
    print('-=-'*10)
    print('{:=^30}'.format('Cadastre uma pessoa'))
    print('-=-'*10)
    idade = int(input('Quantos anos você tem? '))
    print(' - '*10)
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':#Se a resposta for diferente de M e F
        sexo = str(input('\033[1;31mOpção inválida!!\033[m Qual seu sexo? [M/F] ')).strip().upper()[0]
    print(' - '*10)

    #Adicionar as estatísticas
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

    resp = str(input('Mais gente? [S/N] ')).strip().upper()[0]
    while resp not in 'SN': #Se a resposta tiver sido diferente de par e impar
        resp = str(input('\033[1;31mOpção inválida!\033[m Mais gente? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print()
print('-=-'*10)
print(f'{maior_idade} pessoas são maiores de idade' if maior_idade > 0 else '')
print(f'Há um total de {tot_homens} homens' if tot_homens > 0 else '')
print(f'Há {mulheres_menor_20} mulheres com menos de 20 anos' if mulheres_menor_20 > 0 else '')
print('-=-'*10)
