"""Exercício 3 
Efetue um programa que leia uma frase do teclado e mostre: 
Quantas vezes aparece a letra “E”;
Em que posição aparece o “E” a  primeira vez
Em  que posição aparece o “E” a última vez. 
Note: O espaços entre as palavras da frase também contam."""


frase = input('Escreva uma frase: ')
frase_lower = frase.lower()
print(f'A frase tem {frase_lower.count('e')} Es')
print(f"O primeiro E está na posição {frase_lower.find('e')+1}")
print(f"O último E está na posição {frase_lower.rfind('e')+1}")
