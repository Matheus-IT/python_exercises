'''Dada uma sequencia de n números reais, determinar os números
   que compõem a sequencia e o número de vezes que cada um deles
   ocorre na mesma.'''

map_counter = dict()

while True:
    data = input('Enter a number: ')

    if data == '':
        break

    if data in map_counter:
        map_counter[data] += 1
    else:
        map_counter[data] = 1

for k, v in map_counter.items():
    print(f'Key {k} appears {v} times.')
