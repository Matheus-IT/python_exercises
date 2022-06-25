from math import radians, sin, cos, tan
ang = float(input('\033[32mInforme um ângulo: \033[m'))
#Preciso converter o valor de graus para radianos
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('\033[33mO seno de {} é {:.2f}, o cosseno {:.2f}, e o valor da tangente {:.2f}\033[m'.format(ang, seno, coss, tang))
