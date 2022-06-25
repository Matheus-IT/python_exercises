frase = str(input('Digite uma frase qualquer: ')).strip().upper()
fraseDiv = frase.split() #Separa palavras
junto = ''.join(fraseDiv)#Junta palavras e tira os espaços
print('O inverso de {} é {}'.format(junto, junto[::-1]))#Mostra frase ao contrário
if junto == junto[::-1]:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
