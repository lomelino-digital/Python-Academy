"""Efetue um programa que chama uma função com uma palavra como parâmetro de entrada e devolve essa palavra no formato:
1º carater em maiúscula, 2 carater em minúscula e assim sucessivamente até terminar a leitura da palavra
Programe a função fazAlgo, sabendo que temos o seguinte código:"""

def fazAlgo(frase):
    nova_frase = ""
    uppercase = True
    for character in frase:
        if uppercase:
            nova_frase += character.upper()
        else:
            nova_frase += character.lower()
        uppercase = not uppercase
    return nova_frase

def fazAlgo2(frase):
    nova_frase = ""
    for i in range(len(frase)):
        if i % 2:
            nova_frase += frase[i].lower()
        else:
            nova_frase += frase[i].upper()
    return nova_frase

a_string = input('Introduza uma palavra: ')

devolve = fazAlgo(a_string)
print(devolve)
devolve = fazAlgo2(a_string)
print(devolve)
