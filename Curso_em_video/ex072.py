contagem = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        print()
        num = int(input('Número não suportado. Digite um número entre 0 e 20: '))
    print(contagem[num])
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Resposta incorreta! Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
    print('-='*20)
