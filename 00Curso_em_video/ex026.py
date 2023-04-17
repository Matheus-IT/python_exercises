frase = str(input('\033[31mDigite um frase: \033[m')).strip()
print('\033[33mA letra A aparece {} vezes na frase\033[m'.format(frase.upper().count('A')))
print('\033[34mA primeira letra A aparece na posição {}\033[m'.format(frase.upper().find('A')+1))#Começa contagem com 1
print('\033[32mA última letra A apareceu na posição {}\033[m'.format(frase.upper().rfind('A')+1))#Começa busca da direita, contagem do 1
