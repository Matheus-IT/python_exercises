print('\033[1;34m{:=^40}\033[m'.format(' LOJA OLHOS DA CARA '))
v = float(input('\033[1;33mQual o valor das compras? R$\033[m'))
print('\033[36m-=-'*15)
op = int(input('''\033[1;33mQual a sua condição de pagamento?\033[m
\033[37m[1]-Á vista dinheiro/cheque (10% Desconto)\033[m
\033[36m[2]-Á vista no cartão (5% Desconto)\033[m
\033[37m[3]-Em 2x no cartão (Preço normal)\033[m
\033[36m[4]-3x ou mais no cartão (20% Juros)\033[m
=>'''))
print('\033[36m-=-'*15)
#Calcular a condição de pagamento
if op == 1:
    print('\033[32mSua compra de R${} com 10% de desconto será {:.2f}\033[m'.format(v, v - (0.1 * v))) #10% De desconto
elif op == 2:
    print('\033[32mSua compra de R${} com 5% de desconto será {:.2f}\033[m'.format(v, v - (0.5 * v))) #5% De desconto
elif op == 3:
    print('\033[32mVocê irá pagar , então, R${}\033[m'.format(v))
elif op == 4:
    parcelas = int(input('\033[1;33mEm quantas parcelas você irá pagar? \033[m'))
    vJuros = v + (0.20 * v)
    parcelasJuros = vJuros / parcelas
    print('''\033[32mSua compra será parcelada em {}x de R${:.2f} com juros 
Sua compra de R${} vai custar R${:.2f} no final\033[m'''.format(parcelas, parcelasJuros, v, vJuros))
else:
    print('\033[1;31mOpção inválida de pagamento, tente novamente\033[m')
