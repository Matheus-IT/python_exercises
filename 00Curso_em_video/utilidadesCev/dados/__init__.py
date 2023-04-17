def tirarVirgula(entrada):
    return entrada.replace(',', '.')


def eUmNumero(entrada):
    entrada = tirarVirgula(entrada)
    for carac in entrada:
        if not(carac.isnumeric()) and carac != '.': #Se carac não for numérico nem ponto, não é número
            return False
    return True #Se atender as exigências, considera número


def leiaDinheiro(msg):
    entrada = input(msg).strip()
    while not(eUmNumero(entrada)) or entrada == '':
        print(f'\033[1;31mERRO: "{entrada}" é um preço inválido!\033[m')
        entrada = input(msg).strip()
    entrada = tirarVirgula(entrada)
    return float(entrada)
