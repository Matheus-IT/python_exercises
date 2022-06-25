a = float(input('\033[1;31mDigite o primeiro segmento: \033[m'))
b = float(input('\033[1;34mDigite o segundo segmento: \033[m'))
c = float(input('\033[1;32mDigite o terceiro segmento: \033[m'))
print('\033[1;33m-=-\033[m' * 15)

if a < (b + c) and b < (a + c) and c < (a + b):
    print('\033[1;35mEsses segmentos podem formar um triângulo\033[m')
else:
    print('\033[1;36mEsses segmentos não podem formar um triângulo\033[m')
