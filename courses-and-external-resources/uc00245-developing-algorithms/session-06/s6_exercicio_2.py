""" Crie um programa que pergunte ao utilizador, quantos elementos terá uma lista
inicialmente vazia. Conforme o nº de elementos, o programa vai pedindo que sejam
inseridos valores inteiros. Os valores devem ser inseridos na lista. O programa deverá
devolver a lista de números inseridos de forma ordenada."""



def numero_elementos():
    while True:
        numero = input('Diga o número de elementos que deve ter na lista: ')
        if numero.isdecimal():
            break
        print("\n Selecione um número inteiro de elementos.")
        continue
    return int(numero)


def inserir_numeros(numero,lista):
    print(f'Agora diga quais os {numero} elemenetos da lista: ')
    indice = 0
    while indice < numero:
        while True:
            elemento = input(f'Introduza o elemento número {indice + 1}: ')
            try:
                elemento = int(elemento)
                lista.append(elemento)
                indice += 1
                break
            except ValueError:
                print('A lista de hoje apenas aceita números inteiros.')
                continue
    return lista



        
numero = numero_elementos()
lista = []
nova_lista=inserir_numeros(numero,lista)
nova_lista.sort()
print(nova_lista)