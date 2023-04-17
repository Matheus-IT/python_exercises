def leiaInt(msg):
    val = 0
    while True:
        try:
            val = int(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar seus dados\033[m')
            break
        except (ValueError, TypeError):
            print('\033[1;31mErro: por favor, digite um número inteiro válido\033[m')
        else:
            break
    return val


def leiaFloat(msg):
    val = 0
    while True:
        try:
            val = float(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar seus dados\033[m')
            break
        except (ValueError, TypeError):
            print('\033[1;31mErro: por favor, digite um número real válido\033[m')
        else:
            break
    return val


#Programa principal
n1 = leiaInt(' - Digite um numero Inteiro: ')
n2 = leiaFloat(' - Digite um numero Real: ')
print(f' - O valor inteiro digitado foi {n1} e o real foi {n2}')
