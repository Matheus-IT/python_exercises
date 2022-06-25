from mostrar_alunos import mostrar

#programa principal
alunos = {'nomes': [], '1nota': [], '2nota': [], '3nota': []}
for cont in range(3):
    alunos['nomes'].append(str(input(f'\n - Digite o nome do {cont+1} aluno: ')))
    alunos['1nota'].append(float(input(f' - Digite a 1 nota do {cont+1} aluno: ')))
    alunos['2nota'].append(float(input(f' - Digite a 2 nota do {cont+1} aluno: ')))
    alunos['3nota'].append(float(input(f' - Digite a 3 nota do {cont+1} aluno: ')))
mostrar(alunos)
