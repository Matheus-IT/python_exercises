def calc_Min(h, m):
    result = 0
    for cont in range(2):
        if h[cont] == 0:
            h[cont] = 24
    if (h[0] == h[1]) and (m[0] > m[1]):
        result += 24*60
    result += 60*(h[1] - h[0]) + (m[1] - m[0])
    return result


#Programa principal
hrs = list()
mnt = list()
for cont in range(2):
    hrs.append(int(input(' - Digite as horas: ')))
    mnt.append(int(input(' - Digite os minutos: ')))
tot_Min = calc_Min(hrs, mnt)
print(f' - Total de minutos de sono: {tot_Min}')
