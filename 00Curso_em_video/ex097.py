def escreva(msg): #Função para escrever linhas de acordo com o tamanho da mensagem
    print('-'*(len(msg)+2))
    print(f'{msg:^{len(msg)+2}}')
    print('-'*(len(msg)+2))


mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
