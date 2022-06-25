def leiaInt(msg):
    from os import system
    system('cls')
    val = str(input(msg)).strip()
    while not(val.isnumeric()):
        val = str(input(' - Valor incorreto!'+msg)).strip()
    val = int(val)
    return val


#Programa principal
n = leiaInt(' - Digite um numero: ')
print(f' - Voce acabou de digitar o numero {n}')
