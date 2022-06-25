aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['média'] = float(input(f'Qual foi sua média {aluno["nome"]}? '))

#Aluno vai estar APROVADO se a média >= 7, de RECUPERAÇÃO se média >= 6 e REPROVADO se média < 6
aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'recuperação' if aluno['média'] >= 6 else 'reprovado'

print('-='*15)
for k, v in aluno.items():
    print(f'- {k} é {v}')
