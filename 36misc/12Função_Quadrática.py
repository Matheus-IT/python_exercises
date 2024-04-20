def disc(a, b, c): #Calcular o discriminante
    delta = (b**2)-4*a*c
    return delta


def raizx1(delta, a, b): #Raiz x1
    x1 = (-b + (delta**1/2)) / (2*a)
    return x1


def raizx2(delta, a, b): #raiz x2
    x2 = (-b - (delta**1/2)) / (2*a)
    return x2


def mostra_discriminante():
    print('O valor do discriminande de \033[1;34m f(x) =',
    f'{va if va!=1 else ""}X²',
    '+' if vb>0 else '',
    f'{vb if vb!=1 else ""}X',
    '+' if vc>0 else '',
    f'{vc if vc!=0 else ""} \033[m é igual a {discriminante}')


#Programa principal
print('\nf(x) = aX² + bx + c')
va = int(input('Digite o valor de a: '))
vb = int(input('Digite o valor de b: '))
vc = int(input('Digite o valor de c: '))
discriminante = disc(va, vb, vc)
mostra_discriminante()
print(f'O valor de \033[1;32mx1\033[m é igual a {raizx1(discriminante, va, vb)}')
print(f'O valor de \033[1;35mx2\033[m é igual a {raizx2(discriminante, va, vb)}')
