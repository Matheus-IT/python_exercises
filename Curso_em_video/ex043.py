peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/altura**2
#Verificar as faixas de imc
if imc < 18.5:
    print('Seu imc está ABAIXO DO PESO ideal!')
elif 18.5 < imc < 25:
    print('Seu imc está no PESO IDEAL')
elif 25 < imc < 30:
    print('Seu imc está com SOBREPESO!')
elif 30 < imc < 40:
    print('Seu imc está em OBESIDADE, cuidado!!')
else:
    print('Seu imc está em OBESIDADE MÓRBIDA, você corre sérios riscos!!')
