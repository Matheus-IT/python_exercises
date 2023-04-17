km = float(input('\033[1;32mQual a distância da viajem Km/h? \033[m'))
#Forma clássica
'''
if km <= 200:
    preco = 0.5 * km #R$0,50 por cada km
else:
    preco = 0.45 * km #R$0,45 por cada km
print('O valor da passagem será de R${:.2f}'.format(preco))
'''
preco = 0.5 * km if km <= 200 else 0.45 * km #Forma simplificada
print('\033[1;36mO valor da passagem será de R${:.2f}\033[m'.format(preco))
