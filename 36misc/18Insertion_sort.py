def preenche_vetor(v):
    from random import randint #Importacao local
    for cont in range(max):
        v.append(0)
        v[cont] = randint(0, 9)


def mostrar_vetor(v):
    for cont in range(max):
        print(f'({v[cont]})', end=' ')


def ordenar(v):
    for i in range(1, max):
        for j in range(0, i-1):
            if v[i] < v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v


''' Programa principal '''
max = (9) # -> "Constante"
vet = list()
preenche_vetor(vet)
print(' - Vetor antes: ', end='')
mostrar_vetor(vet)
print(f'\n - Vetor depois: {ordenar(vet)}')
