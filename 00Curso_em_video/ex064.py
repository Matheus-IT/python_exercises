resp = s = 0
cont = 1 #Contador
while resp != 999:
    resp = int(input('Digite o {}º valor (999 parar): '.format(cont)))
    cont += 1
    if resp != 999:#Desconsiderando 999
        s += resp
cont -= 2 #Desconsiderando 999
print()
print('Foram digitados {} valores'.format(cont))
print('A soma deles é de {}'.format(s))
