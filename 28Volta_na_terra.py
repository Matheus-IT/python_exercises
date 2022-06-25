from time import sleep


kmh = int(input(' - Qual a velocidade em Km/h? '))
um_dia = 18 * kmh #Quilometros por dia com essa velocidade (Menos as seis horas de sono mínimas)
circf_terra = 40075 #Tamanho da circunferencia da terra
dist_total = 0
qtd_dias = 0
print(' - Calculando...')
while dist_total <= circf_terra:
    dist_total += um_dia #Calcula quantos dias pra uma volta na terra
    qtd_dias += 1
    sleep(0.05)
print(f' - Com essa velocidade demoraria mais ou menos {qtd_dias} dias para uma volta completa no mundo')
