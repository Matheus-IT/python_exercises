b = float(input('\033[36mQual a largura da parede? \033[m'))
h = float(input('\033[32mQual a altura da parede? \033[m'))
a = b * h
print('\033[36mSua parede tem dimensão {} x {} e sua área é de {:.3f}m².\033[m'.format(b, h, a))
print('\033[32mPara pintar essa parede, você precisará de {}L de tinta.\033[m'.format(a / 2))
