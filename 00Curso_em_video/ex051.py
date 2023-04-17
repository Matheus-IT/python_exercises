from time import sleep
termo1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao): #Mostra os dez primeiros termos de uma pa
    print(' {} '.format(c), end='=>')
    sleep(0.3)
print(' Acabou')
