from random import shuffle

a1 = input('\033[31mNome do primeiro aluno: \033[m')
a2 = input('\033[32mNome do segundo aluno: \033[m')
a3 = input('\033[33mNome do terceiro aluno: \033[m')
a4 = input('\033[34mNome do quarto aluno: \033[m')

#Coloca os alunos em uma lista
lista = [a1, a2, a3, a4]
#Embaralha a lista
shuffle(lista)

print('\033[36m{}\033[m'.format(lista))
