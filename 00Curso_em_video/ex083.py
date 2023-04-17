lista = []
parent_left = 0
parent_right = 0
lista = list(str(input('Digite sua expressão: ')))
for v in lista:
    if v == '(': #Acumular o número de parênteses a esquerda
        parent_left += 1
    if v == ')': #Acumular o número de parênteses a direita
        parent_right += 1
if parent_left == parent_right: #Para cada parêntese aberto precisa-se de um que esteja fechado
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')
