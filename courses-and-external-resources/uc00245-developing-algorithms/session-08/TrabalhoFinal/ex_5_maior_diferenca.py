def introduzir_numero():
    while True:
        print('Introduza um número:')
        numero = input()
        numero = numero.replace(',','.')
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('Não introduziu um número')

def continuar():
    while True:
        print('\nDeseja acrescentar mais um número (s/n)?')
        resposta = input()
        resposta = resposta.lower()
        if resposta == 's' or resposta == 'n':
            if resposta == 's':
                return True
            return False
        print('Selecione s para sim ou n para não.')



def construir_lista():
    lista = []
    while True:
        numero = introduzir_numero()
        lista.append(numero)
        
        if not continuar():
            print(f"Escolheu a lista {lista}")
            return lista
    

def maior_diferenca(lista):
    diferencas_max = 0
    lista_de_trabalho = lista.copy()
    if len(lista) < 2:
        print("A sua lista é demasiado pequena para calcular diferenças")
        return 0
    for num in lista:
        lista_de_trabalho.remove(num)
        for num2 in lista_de_trabalho:
            diferenca = abs(num - num2)
            if diferenca > diferencas_max:
                diferencas_max = diferenca

    return diferencas_max


lista = construir_lista()

maior = maior_diferenca(lista)

print(f"A maior diferença na sua lista é {maior}")
            
