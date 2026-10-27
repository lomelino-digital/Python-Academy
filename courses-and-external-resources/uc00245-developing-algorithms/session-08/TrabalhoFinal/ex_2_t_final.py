
def pedir_numero():
    while True:
        linhas = input('Qual o nunero de linhas deseja? ')
        if linhas.isdecimal():
            break
        print('Por favor selecione um numero inteiro de linhas.\n')        
    return int(linhas)
    
def estrelas(numero_de_linhas):
    for i in range(numero_de_linhas):
        print((i+1)*'*')




numero_utilizador = pedir_numero()
estrelas(numero_utilizador)