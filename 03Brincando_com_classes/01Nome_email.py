class Usuario:
    cont = 0
    def __init__(self, n, e): #Parâmetros recebidos pelo usuário: 'n' 'e'
        Usuario.cont += 1
        self.nome = n
        self.email = e
    
    def diga_ola(self):
        print(f'Olá meu nome é {self.nome}, o meu email é {self.email}')
        try: #Tenta mostrar idade, alguns objetos não tem idade
            print(f'E minha idade é {self.idade}')
        except:
            pass


def registrar_pessoa(pessoa):
    nome = str(input(' - Nome: ')).strip().title()
    email = str(input(' - Email: ')).strip()
    pessoa.append(Usuario(nome, email)) #Pessoa[c] pertence a classe usuario


pessoa = []
for c in range(4): #Registrar 2 pessoas
    print(f'= Registrar {c+1} pessoa ='.center(30))
    registrar_pessoa(pessoa)
#Definir/criar atributo do objeto
pessoa[0].idade = 18 #Posso fazer desse jeito
setattr(pessoa[1], 'idade', 19) #Ou desse jeito
for c in range(Usuario.cont):
    pessoa[c].diga_ola() #Nos métodos preciso colocar parenteses
print(f'Foram registradas {Usuario.cont} pessoas')
