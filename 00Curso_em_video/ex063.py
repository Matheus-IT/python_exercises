print('{:=^30}'.format('Sequência Fibonacci'))
n = int(input('Quer ver quantos termos? '))
a = 1
b = 0
prox = 1
termos = 0
while termos < n:
    print(prox)
    prox = a + b #O prox é resultado da soma dos dois anteriores
    b = a
    a = prox
    termos += 1 #Cada termo é resultado desse while
