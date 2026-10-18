"""4. Implemente um programa que pede ao utilizador uma lista com valores inteiros e que
invoca a função media(lista)para efetuar o cálculo da média desses valores."""

def media(lista):
    total = 0
    for n in lista:
        total += int(n) 
    if len(lista) == 0:
        return 'Lista vazia.'
    return total/len(lista)

lista = input("Indique a lista de numeros que pretende fazer a média: ")
lista = lista.split()

print(media(lista))