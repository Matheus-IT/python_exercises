km = float(input('\033[33mQuantos Km percorridos? \033[m'))
d = float(input('\033[32mQuantos dias ele foi alugado? \033[m'))
# Custa R$60 por dia e R$0,15 por km
pkm = km * 0.15
pd = d * 60
print('\033[31mTotal a pagar pelo aluguel é de R${:.2f}\033[m'.format(pkm + pd))
