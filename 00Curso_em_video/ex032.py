from datetime import date
ano = int(input('\033[1;35mQual ano deseja verificar?(0 para analisar o ano atual da máquina): \033[m'))
if ano == 0:
    ano = date.today().year #Pega o ano atual da máquina
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('\033[1;33mO ano de {} é bissexto!\033[m'.format(ano))
else:
    print('\033[1;34mO ano de {} não é bissexto!\033[m'.format(ano))
