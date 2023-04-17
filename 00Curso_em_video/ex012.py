prod = float(input('\033[1;36mQual o preço do produto? R$\033[m'))
desc = prod * 5 / 100
print('\033[1;32mO produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}\033[m'.format(prod, prod - desc))
