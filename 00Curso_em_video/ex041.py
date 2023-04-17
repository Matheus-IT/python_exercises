from datetime import date
anoNasc = int(input('Qual sua data de nascimento? '))
idade = date.today().year - anoNasc
print('Quem nasceu em {} tem {} anos'.format(anoNasc, idade))
#Categorias para nadadores
if idade < 9:
    print('Sua categoria é nadador MIRIM')
elif idade <= 14:
    print('Sua categoria é nadador INFANTIL')
elif idade <= 19:
    print('Sua categoria é nadador JUNIOR')
elif idade <= 25:
    print('Sua categoria é nadador SÊNIOR')
else:
    print('Sua categoria é nadador MASTER')
