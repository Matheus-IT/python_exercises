n = int(input('\033[1;35mMe diga um número qualquer: \033[m'))
if n % 2 == 0:
    print('\033[1;32mO número {} é PAR\033[m'.format(n))
else:
    print('\033[1;36mO número {} é ÍMPAR\033[m'.format(n))
