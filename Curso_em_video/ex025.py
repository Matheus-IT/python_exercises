name = input('\033[32mQual é o seu nome completo? \033[m').strip()#To remove spaces on the begin or final
print('\033[33mSeu nome tem Silva? {}\033[m'.format('SILVA' in name.upper().split()))
