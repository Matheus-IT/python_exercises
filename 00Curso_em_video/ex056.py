sAge = 0
older = 0
olderMan = ''
woman20 = 0
for c in range(1, 5):
    name = str(input('{}-Qual o seu nome? '.format(c)))
    age = int(input('{}-Qual a sua idade? '.format(c)))
    sAge += age
    gender = int(input('{}-Qual o seu sexo? [1:M/2:F]'.format(c)))
    if (gender == 2) and (age < 20):#Quantas mulheres tem menos de 20 anos
        woman20 += 1
    if (gender == 1) and (age > older):#Idade do homem mais velho
        older = age
    if (gender == 1) and (age >= older):#Se o homem atual for mais velho que o homem mais velho, este será o mais velho
        olderMan = name
    print()
print('A média de idade desse grupo é de {} anos'.format(sAge / 4))#Média de idade do grupo
if olderMan != '':
    print('E o homem mais velho do grupo é {} e tem {} anos'.format(olderMan, older))
if woman20 != 0:
    print('As mulheres que tem menos de 20 anos foram {}'.format(woman20))
