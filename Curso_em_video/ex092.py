from datetime import date
#Retornar: {nome; idade; carteira de trabalho; contratação; salário; aposentadoria}
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).strip().title() #Guardar no campo 'nome' do dicionário 'trabalhador'
aNasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - aNasc #trabalhador['idade'] = A_atual - A_nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if trabalhador['ctps'] != 0: #Se tiver carteira de trabalho
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário do trabalhador: '))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] + 35) - aNasc #idade_aposent = A_aposent - aNasc

print('-='*15)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
print('-='*15)
