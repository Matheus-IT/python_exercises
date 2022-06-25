nome = str(input('\033[31mDigite seu nome completo: \033[m')).strip()#Remover os espaços em branco do começo e do final
print('\033[32mO seu nome em maiúsculas é: {}\033[m'.format(nome.upper()))
print('\033[33mO seu nome em minusculas é: {}\033[m'.format(nome.lower()))
print('\033[34mAo todo seu nome tem {} letras\033[m'.format(len(nome.replace(' ', ''))))
div = nome.split()
print('\033[35mSeu primeiro nome é {} e ele tem {} letras\033[m'.format(div[0].title(), len(div[0])))
