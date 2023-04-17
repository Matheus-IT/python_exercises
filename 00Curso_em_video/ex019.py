from random import choice
a1 = input('\033[1;32mPrimeiro aluno: \033[m')
a2 = input('\033[1;31mSegundo aluno: \033[m')
a3 = input('\033[1;33mTerceiro aluno: \033[m')
a4 = input('\033[1;35mQuarto aluno: \033[m')

#Criar uma lista de alunos
lista = [a1, a2, a3, a4]
#Escolher um aluno da lista
escolhido = choice(lista)

print('\033[1;36mO aluno escolhido foi: {}\033[m'.format(escolhido))
