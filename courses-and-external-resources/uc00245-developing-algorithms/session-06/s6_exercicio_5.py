"""5. Inicialize uma lista de 20 números inteiros. Armazene os números pares numa lista PAR
e os números ímpares numa lista ÍMPAR. Apresente as listas PAR e IMPAR.
for n in lista:
        if n % 2:
            lista_impares.append(n)
        else:
            lista_pares.append(n)

"""

def pares_impares(lista):
    lista_pares = [n for n in lista if n % 2 == 0 ]
    lista_impares = [n for n in lista if n % 2 ]
    return lista_pares,lista_impares


lista = list(range(1,21))

PAR, IMPAR = pares_impares(lista)

print(f"A lista par é {PAR}")
print(f"A lista impar é {IMPAR}")