import funcoes as fc
from os import system
from time import sleep


op = None
file_name = '06Arquivos_csv/lista_pessoas.csv'
if not fc.arquivo_criado(file_name): #Se o arquivo não tiver sido criado
        f = open(file_name, 'w') #Cria arquivo
        f.close()
fc.mostra_menu()
op = fc.opcoes()
while True:
    if op == 1:
        fc.mostra_menu()
        sleep(1)
        fc.mostra_lista(file_name)
        op = fc.opcoes()
    elif op == 2:
        fc.mostra_menu()
        fc.cadastrar_pessoa(file_name)
        fc.mostra_lista(file_name)
        op = fc.opcoes()
    elif op == 3:
        fc.mostra_menu()
        qtd_pessoas = fc.mostra_lista(file_name)
        fc.tirar_pessoa(file_name, qtd_pessoas)
        op = fc.opcoes()
    elif op == 4:
        break
    else:
        fc.mostra_menu()
        print(' - Nao entendi')
        op = fc.opcoes()
