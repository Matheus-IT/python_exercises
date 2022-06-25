import moeda

preco = float(input(' - Digite um preco \033[1;32mR$\033[m: '))
print(f' - A metade de {preco} e {moeda.metade(preco)}')
print(f' - O dobro de {preco} e {moeda.dobro(preco)}')
print(f' - Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f' - Diminuindo 13%, temos {moeda.diminuir(preco, 13)}')
