def voto(a_n):
    """Função para retornar uma frase de
     acordo com a situação eleitoral"""
    from datetime import date #Importacao com escopo local
    a_atual = date.today().year
    idade = a_atual - a_n
    if (16 <= idade < 18) or idade > 70:
        return f'Com {idade} o voto é opcional'
    elif idade < 16:
        return f'Com {idade} você ainda não vota'
    elif 18 <= idade < 70:
        return f'Com {idade} o voto é obrigatório'


a_nasc = int(input('Qual o seu ano de nascimento? '))
print(voto(a_nasc))
