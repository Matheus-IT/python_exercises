from funcoes import resumo_carro
 

class Carro:
    '''Essa classe define uma fôrma para Carro'''
    def __init__(self): #Esse é o método construtor
        self.modelo = ''
        self.cor = 'Vermelho'
        self.vidros_eletricos = False
        self.travas_eletricas = True
        self.qtd_lugares = 5
        self.gps = True


class Golf_gti(Carro):
    def __init__(self):
        Carro.__init__(self) #Gol herda atributos de Carro
        self.modelo = 'Golf gti'


class Lamborghini_gallardo(Carro):
    def __init__(self):
        Carro.__init__(self)
        self.modelo = 'Lamborghini gallardo'
        self.cor = 'Dourado'
        self.qtd_lugares = 2
        self.vidros_eletricos = True


class Maserati_levante(Carro):
    def __init__(self):
        Carro.__init__(self)
        self.modelo = 'Maserati levante'
        self.cor = "Azul"
        self.qtd_lugares = 4
        self.vidros_eletricos = True
        self.camera_de_re = True


class Porshe_911_Carrera(Maserati_levante):
    def __init__(self):
        Maserati_levante.__init__(self) #O porshe herda de Maserati
        self.modelo = 'Porshe 911 Carrera'
        self.wifi = True


print('='*30)
print('Consencionaria Carro Novo'.center(30))
print('='*30)
print(' - Escolha um carro: ')
print('[1] Golf gti\
    [2] Lamborghini gallardo\
    [3] Maserati levante\
    [4] Porshe 911 Carrera')
escolha = int(input('=> Sua escolha: '))
if escolha == 1:
    c = Golf_gti()
elif escolha == 2:
    c = Lamborghini_gallardo()
elif escolha == 3:
    c = Maserati_levante()
elif escolha == 4:
    c = Porshe_911_Carrera()
else:
    print('Nao entendi :(')
resumo_carro(c)
