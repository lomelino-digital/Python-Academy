"""Crie um programa que peça ao utilizador que insira um valor inteiro válido,
seguido de um Real(float) válido.
a. O programa só pode avançar caso os valores inseridos sejam
mesmo válidos. Crie as excepções adequadas e garanta que o
programa não avança, caso os dados inseridos estejam
incorretos."""


def introduzir_numero():
    while True:
        print('Introduza um número:')
        numero = input()
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('Não introduziu um número')

def introduzir_inteiro():
    while True:
        print('Apenas aceita números inteiros')
        numero = introduzir_numero()
        if numero.is_integer:
            return int(numero)
        print('Não introduziu um número inteiro.\n')


introduzir_inteiro()
        
