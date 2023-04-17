sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]#Primeira letra
while sexo != 'M' and sexo != 'F':
    print('\033[1;31mOpção incorreta! Digite novamente!\033[m')
    sexo = str(input('Qual o seu sexo [M/F]? ')).upper()
print('\033[1;34mSexo {} registrado com sucesso\033[m'.format(sexo))
