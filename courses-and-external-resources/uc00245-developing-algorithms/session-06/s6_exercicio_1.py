"""1. Implemente a função max_lista(lista). A função recebe um argumento com uma lista
dos valores numéricos e retorna o maior desses valores, ou zero se a lista estiver vazia.
Apresente uma solução com o ciclo While e outra com o ciclo FOR"""

def max_lista(lista):
    if lista:
        max = lista[0]
    else:
        return 0
    for n in lista:            
        if n > max:
            max = n
    return max


def max_lista_while(lista):
    if lista:
        max = lista[0]
    else:
        return 0
    i = 0
    while i < len(lista):
        if lista[i] > max:
            max = lista[i]
        i += 1
    return max
        


def test(lista):
    print(f"Max com for: {max_lista(lista)}")
    print(f"Max com while: {max_lista_while(lista)}")

test([])
test([-1,-5,-77,-9,-7])
test([42])
test([-1,7,-9,0,-6])
test([1,5,7,9,99])
test([1,6,7,88,88])
test([1,6,7,-1,-1])