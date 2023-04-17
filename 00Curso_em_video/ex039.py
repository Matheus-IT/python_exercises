import datetime
aNasc = int(input('Qual o seu ano de nascimento? '))
data = datetime.date.today().year
idade = data - aNasc
sexo = str(input('Qual o seu sexo? [M/F]'))
sexo = sexo.title()
print('Quem nasceu em {} tem {} anos em {}'.format(aNasc, idade, data))
if sexo == 'F':
    print('Como seu sexo é feminino, o alistamento militar não é obrigatório')
else:
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento será em {}'.format(data + (18 - idade)))
    elif idade > 18:
        print('Você deveria ter se alistado há {} anos'.format(idade - 18))
        print('Seu alistamento ocorreu no ano de {}'.format(data - (idade - 18)))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
