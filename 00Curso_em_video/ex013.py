sal = float(input('\033[1;37mQual é o salário do funcionário?\033[m'))
nsal = sal + (sal * 15/100)
print('\033[1;34mUm funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, nsal))
