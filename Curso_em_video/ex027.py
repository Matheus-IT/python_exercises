nome = str(input('\033[1;3mDigite seu nome completo: \033[m')).strip()
print('\033[1;34mMuito prazer em te conhecer!\033[m')
div = nome.split()
print('\033[31mSeu primeiro nome é {}\033[m'.format(div[0].title()))
print('\033[32mSeu último nome é {}\033[m'.format(div[len(div)-1].title()))
