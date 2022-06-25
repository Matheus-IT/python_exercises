class Person():
    def __init__(self, n='', cit='', phon=0, mail='@gmail.com'):
        self.name: str = n
        self.city: str = cit
        self.phone = phon
        self.e_mail: str = mail

    def __str__(self):
        return f'Hi! My name is {self.name} and I live in {self.city}'

    def __del__(self):
        print('See you later!')


p = Person('Matthew', 'Parnaiba', 15364875, 'myemail@gmail.com')
print(p)
del p
