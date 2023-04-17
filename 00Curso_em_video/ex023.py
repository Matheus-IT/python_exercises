n = int(input('\033[1;36mInforme um número inteiro: \033[m'))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('\033[1;31mUnidade {}\033[m'.format(u))
print('\033[1;32mDezena {}\033[m'.format(d))
print('\033[1;35mCentena {}\033[m'.format(c))
print('\033[1;34mMilhar {}\033[m'.format(m))
