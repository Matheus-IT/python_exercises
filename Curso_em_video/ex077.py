lista_palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in lista_palavras: #Para cada palavra na lista de palavras
    print(f'\nNa palavra \033[1;32m{palavra}\033[m temos ', end='') #Mostramos a palavra e as suas vogais
    for letra in palavra: #Olhar em cada letra da palavra
        if letra in 'AEIOU': #Se a letra for uma vogal
            print('\033[1;34m{}\033[m'.format(letra.lower()), end=' ')
