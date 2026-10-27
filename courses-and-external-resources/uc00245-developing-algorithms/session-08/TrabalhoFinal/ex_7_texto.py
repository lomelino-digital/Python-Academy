"""Cria uma função que recebe um texto e devolve:
• Quantas palavras tem;
• A palavra mais longa;
• Quantas vezes cada letra aparece (usa um dicionário para contar).
Exemplo com o texto "Olá, o mundo da programação!":
Palavras: 5
Mais longa: programação!
Contagem de letras: {'o': 5, 'l': 1, 'á': 1, 'm': 2, 'u': 1, 'n': 1, 'd': 2, 'a': 3, 'p': 1, 'r': 2, 'g': 1, 'ç': 1, 'ã':
1"""


def numero_de_palavras(frase):
    return len(frase.split())

def palavra_mais_longa(frase):
    mais_longa = ""
    for word in frase.split():
        if len(word) > len(mais_longa):
            mais_longa = word
    return mais_longa

def contagem_de_letras(frase):
    contagem_de_letras = {}
    for char in frase:
        if char.isalpha():
            char = char.lower()
            contagem_de_letras[char] = contagem_de_letras.get(char, 0) + 1
    return contagem_de_letras



frase = input('Introduza uma frase para analisar: ')

print(f"Palavras: {numero_de_palavras(frase)}")
print(f"Mais longa: {palavra_mais_longa(frase)}")
print(f"Contagem de letras: {contagem_de_letras(frase)}")
