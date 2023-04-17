nome_alunos = list()
notas_alunos = [[], []]
nome = ''
media = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    nome_alunos.append(nome)
    notas_alunos[0].append(float(input('Nota 1: '))) #Guardar a PRIMEIRA nota do aluno atual
    notas_alunos[1].append(float(input('Nota 2: '))) #Guardar a SEGUNDA nota do aluno atual

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN': #Tratando erros de digitação
        resp = str(input('\033[1;31mOpção inválida!\033[m Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N' or 'Não':
        break

print('-=-'*11)
for c in range(0, len(nome_alunos)):
    media = (notas_alunos[0][c] + notas_alunos[1][c])/2 #Cálculo da média
    print(f'{c+1:2}ºAluno: \033[1;34m{nome_alunos[c]:10}\033[m Média:\033[1;32m{media:<5.1f}\033[m')
print('-=-'*11)

while True:
    resp = int(input('Mostrar notas de qual aluno? (999:parar) '))
    if resp == 999: #Verificar se a resposta foi o FLAG
        print('\033[1;33mFinalizando...\033[m')
        break
    if resp <= len(nome_alunos):
        print('-=-' * 11)
        print(f'Notas de \033[1;34m{nome_alunos[resp-1]}\033[m: \033[1;32m{notas_alunos[0][resp-1]}, {notas_alunos[1][resp-1]}\033[m')
    else:
        print('\033[1;31mO aluno correspondente não existe!\033[m')
