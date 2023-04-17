a = float(input('\033[1;33mDigite o primeiro segmento: \033[m'))
b = float(input('\033[1;34mDigite o segundo segmento: \033[m'))
c = float(input('\033[1;31mDigite o terceiro segmento: \033[1;35m'))
print('\033[37m-=-\033[37m'*15)
#Verifica se os segmentos podem formar um triângulo
if a < (b + c) and b < (a + c) and c < (a + b):
    print('\033[36mEsses segmentos podem formar um triângulo!\033[m')
    # Verifica qual o tipo de triângulo será formado
    if a == b == c:
        print('\033[1;36mO triângulo formado é EQUILÁTERO\033[m')
    elif (a == b) or (b == c) or (a == c):
        print('\033[1;34mO triângulo formado é ISÓSCELES\033[m')
    else:
        print('\033[1;35mO triângulo formado é ESCALENO\033[m')
else:
    print('\033[1;31mEsses segmentos não podem formar um triângulo!\033[m')
