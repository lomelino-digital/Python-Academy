"""Exercício 2
Efetue um programa que leia o nome de uma pessoa e averigue se ela tem a palavra “Pereira” no nome."""

nome = input('Introduza o seu nome: ')
if 'pereira' in nome.lower():
    print('true')
else:
    print('false')