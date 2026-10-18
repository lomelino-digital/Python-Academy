"""Exercício 1 
Crie um programa que leia o seu nome completo e mostre:
- O nome lido em maiúsculas;
- O nome lido em minúsculas;
- Quantas letras tem o primeiro nome
- Mostre o primeiro nome
- Mostre o último nome  """

nome = input('Introduza o seu nome: ')
nome_lista = nome.split()
print('O nome em maiúsculas é:', end=' ')
print(nome.upper())
print('O nome em minúsculas é:', end=' ')
print(nome.lower())
print( "o primeiro nome tem", len(nome_lista[0]), "letras")
print('O primeiro nome é:', end=' ')
print(nome_lista[0])
print('O último nome é:', end=' ')
print(nome_lista[-1])