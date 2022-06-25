from math import sqrt


def decorate_message(msg:str):
    def gen_symbol():
        symbols = ('-', '*', '=', '#')

        for symbol in symbols:
            yield symbol

    def line_half_word(word:str):
        symbol = next(gen_symbol())
        return symbol*(len(word) // 2)
    
    decorated_message =  line_half_word(msg) \
                                + msg + \
                         line_half_word(msg)
    
    def do_the_job():
        print(decorated_message)
    do_the_job()


decorate_message('Cálculo das raízes de uma equação do 2º grau')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a != 0.0:
    delta = b**2 - 4 * a * c
    
    if delta >= 0.0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        
        print('As raízes são:')
        print('x1 = ', x1)
        print('x2 = ', x2)
    else:
        print('Não existem raízes reais!')
else:
    print('A expressão é uma equação do 1º grau')
    print('Raiz =', -c / b)