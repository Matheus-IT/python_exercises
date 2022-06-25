from utilidadesCev import moeda #Usando pacotes
from utilidadesCev import dados

preco = dados.leiaDinheiro(' - Digite um preco \033[1;32mR$\033[m: ')
moeda.resumo(preco, 80, 35)
