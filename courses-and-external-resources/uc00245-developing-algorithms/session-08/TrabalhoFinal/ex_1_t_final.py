"""Exercício 1

Peça ao utilizador para introduzir uma sequência de 5 números inteiros. 
Utilize um ciclo for e a instrução continue para imprimir apenas os números pares da sequência.

Exemplo de Interação: Introduza 5 números: 
Número 1: 3 
Número 2: 8 
Número 3: 1
Número 4: 4
Número 5: 9 

Números pares: 8, 4"""

def introduzir_numero(n):
    while True:
        numero = input(f"Numero {n+1}: ")
        if numero.isdecimal():
            break
        print('Introduza um número inteiro.\n')
        continue
    return numero

def numero_de_numeros():    
    while True:
        numeros = input('Introduza o numero de numeros a testar: ')
        if numeros.isdecimal():
            break
        print('Introduza um número inteiro.\n')
        continue
    return int(numeros)



num = numero_de_numeros()

print(f"Introduza {num} números inteiros.")

numeros = []
lista_pares = []
for n in range(num):
    numeros.append(introduzir_numero(n))

for numero in numeros:
    if int(numero) % 2 != 0:
        continue
    lista_pares.append(numero)

print(f"Números pares: {', '.join(lista_pares)}")




