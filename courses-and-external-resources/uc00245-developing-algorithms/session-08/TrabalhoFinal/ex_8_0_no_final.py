"""A partir de uma dada lista de números, reorganizá-la de modo a colocar todos os zeros no final,
mantendo a ordem dos restantes elementos.
numeros = [0, 4, 0, 2, 7, 0, 1]
Resultado: [4, 2, 7, 1, 0, 0, 0]"""


def zeros_no_final(lista):
    nova_lista = lista.copy()
    for n in lista:
        if n == 0:
            nova_lista.remove(n)
            nova_lista.append(0)
    return nova_lista


def construir_lista():
    lista = []
    while True:
        numero = introduzir_numero()
        lista.append(numero)
        
        if not continuar():
            print(f"Escolheu a lista {lista}")
            return lista


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


numeros = [0, 4, 0, 2, 7, 0, 1]

print(zeros_no_final(numeros))

while True:
        print('\nDeseja introduzir a sua lista (s/n)?')
        resposta = input()
        resposta = resposta.lower()
        if resposta == 's' or resposta == 'n':
            if resposta == 's':
                numeros = construir_lista()
                print(zeros_no_final(numeros))
            else:
                break
        else:
            print('Não tem a certeza?')
            continue