from datetime import date
import emoji
maiores = 0
menores = 0
for c in range(1, 7 + 1):
    anoNasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = date.today().year - anoNasc
    if idade >= 21:
        maiores += 1 #Tot maiores de idade
    else:
        menores += 1#Tot menores de idade
print(emoji.emojize('''\033[1;32mHá um total de {} pessoas maiores de idade :man:\033[m
\033[1;34mE {} pessoas menores de idade :boy:\033[m'''.format(maiores, menores)))
