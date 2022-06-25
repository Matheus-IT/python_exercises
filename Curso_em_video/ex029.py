velocidade = float(input('\033[1;36mQual a velocidade atual do carro? \033[m'))
multa = (velocidade - 80)*7#Sete reais pra cada km acima de 80
if velocidade > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido de 80Km/h\033[m')
    print('\033[1;36mVocê deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
print('\033[1;30mTenha um bom dia, dirija com segurança\033[m')
