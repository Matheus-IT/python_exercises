from time import sleep


def maior(*valores):
    print('-='*30)
    print('Analisando os valores...')
    sleep(1.5)
    c = 0
    while c < len(valores):
        print(valores[c], end=' ')
        c += 1
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {max(valores) if len(valores) > 0 else 0}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
