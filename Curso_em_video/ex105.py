from os import system


def notas(*vals,sit=False):
    aluno = dict()
    aluno['Total'] = len(vals)
    aluno['Maior'] = max(vals)
    aluno['Menor'] = min(vals)
    aluno['Media'] = sum(vals) / len(vals)
    if (aluno['Media'] >= 0) and (aluno['Media'] < 6):
        aluno['Situacao'] = 'Ruim'
    elif (aluno['Media'] >= 6) and (aluno['Media'] <= 7):
        aluno['Situacao'] = 'Razoavel'
    elif (aluno['Media'] > 7):
        aluno['Situacao'] = 'Boa'
    else:
        aluno['Situacao'] = 'Erro'
    return aluno


#Programa principal
system('cls')
resp = notas(5.7, 9.5, 8.0, 7.75, 5.5, sit=True)
print('{:=^19}'.format(' Resultado '))
for i in resp:
    if i == 'Situacao':
        print(f' - {i}: {resp[i]}')
    else:
        print(f' - {i}: {resp[i]:.2f}')
