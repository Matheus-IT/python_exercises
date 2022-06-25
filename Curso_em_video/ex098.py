from time import sleep


def contador(ini, fim, pas):
    print('-='*30)
    if pas == 0: #Evitar erro se for digitado 0
        pas = 1
    pas = abs(pas) #Pegar a parte positiva de pas
    print(f'Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}')
    for c in range(ini, fim+1 if (ini < fim) else fim-1, pas if (ini < fim) else -pas):
        print(c, end=' ')
        sleep(0.4)
    print('Fim!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
