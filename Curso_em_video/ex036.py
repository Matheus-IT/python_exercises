print('\033[1;31m-=-\033[m'*15)
print('\033[1;35m            Banco Javali Cansado\033[m')
print('\033[1;31m-=-\033[m'*15)
valCasa = float(input('\033[1;34mOlá, qual o valor da casa que você deseja? R$\033[m'))
sal = float(input('\033[1;32mInforme o seu salário: R$\033[m'))
anos = int(input('\033[1;36mEm quantos anos você quer pagar? \033[m'))
meses = anos * 12
mensalidade = valCasa / meses

print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valCasa, anos, mensalidade))
if mensalidade < (0.3 * sal): #Se a mensalidade for MENOR que 30% do salário o empréstimo será aprovado
    print('\033[1;32mEmpréstimo aprovado!!\033[m')
else:
    print('\033[1;31mEmpréstimo negado\033[m')
