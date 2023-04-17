n1 = float(input('\033[1;31mDigite a primeira nota: \033[m'))
n2 = float(input('\033[1;34mDigite a segunda nota: \033[m'))
print()
m = (n1 + n2)/2
print('Primeira nota {:.1f}, segunda nota {:.1f}, a média então será {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO!')
elif 6.9 > m >= 5: #Média está entre  5 e 6.9
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
