from time import sleep


alunos = {'Nomes':[], 'Nota1':[], 'Nota2':[], 'Nota3':[], 'Media':[]}
for cont in range(3):
    alunos['Nomes'].append(str(input(f' - Digite o nome do {cont+1}o aluno: ')))
    alunos['Nota1'].append(float(input(f' - Digite a {cont+1}o nota: ')))
    alunos['Nota2'].append(float(input(f' - Digite a {cont+1}o nota: ')))
    alunos['Nota3'].append(float(input(f' - Digite a {cont+1}o nota: ')))
for cont in range(3):
    print(f'Notas de {alunos["Nomes"][cont]}', end=' ')
    print(f'1o {alunos["Nota1"][cont]}', end=' ')
    print(f'2o {alunos["Nota2"][cont]}', end=' ')
    print(f'3o {alunos["Nota3"][cont]}', end=' ')
    m = (alunos['Nota1'][cont]+(alunos['Nota2'][cont]*2)+(alunos['Nota3'][cont]*3))/6
    print(f'Media {m:4.2f}')
    sleep(0.5)
