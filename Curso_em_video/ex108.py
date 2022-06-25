import moeda

preco = float(input(' - Digite um preco \033[1;32mR$\033[m: '))
print(f' - A metade de {moeda.moeda(preco)} e {moeda.moeda(moeda.metade(preco))}')
print(f' - O dobro de {moeda.moeda(preco)} e {moeda.moeda(moeda.dobro(preco))}')
print(f' - Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f' - Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}')
