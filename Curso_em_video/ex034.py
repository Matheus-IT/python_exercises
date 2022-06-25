sal = float(input('\033[35mQual o seu salário? R$\033[m'))
if sal <= 1250:
    aumento = sal + (0.15 * sal)
else:
    aumento = sal + (0.10 * sal)
print('\033[1;35mQuem ganhava R${:.2f} passa a ganhar R${:.2f} agora\033[m'.format(sal, aumento))
