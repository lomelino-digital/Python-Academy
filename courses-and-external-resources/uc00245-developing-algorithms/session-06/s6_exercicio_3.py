"""Dada uma lista de números, localize e apresente os elementos que existam na lista
mais do que uma vez. Os números devem ser apresentados pela ordem na lista original.
Caso não haja nenhum número nessas condições, o utilizador deverá ser informado."""


def contar(lista):
    for x in lista:
        vezes = lista.count(x)
        if vezes == 1:
            print(f"{x} aparece apenas uma vez")
        elif x > 1:
            print(f"{x} aparece {vezes} vezes")
            i = 0
            while i < vezes:
                lista.remove(x)
                i += 1



print(contar([1,5,7,3,2,8,9,4,5,3,2]))
      