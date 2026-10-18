"""Altere o programa nº3, aumentando o intervalo entre 0 e 100, mas desta vez, 
vá dando dicas ao utilizador, se o nº inserido por ele é: (“Mais Alto” ou “Mais Baixo”) do que o gerado. 
Quando o utilizador acertar no número, deverá surgir “Acertou!!” e em quantas tentativas foi."""

import random

numero = random.randint(0,100)
tentativas = 0
def pedir_palpite(tentativas):    
    adivinhar = input('Adivinhe o número: ')
    tentativas += 1
    while True:
        try:
            adivinhar = int(adivinhar)
            if not (0 <= adivinhar <= 100):
                raise ValueError
        except ValueError:        
            print('Escolha inválida, escolha um número inteiro entre 0 e 100')       
            continue
        else:
            return adivinhar, tentativas

adivinhar, tentativas = pedir_palpite(tentativas)

while int(adivinhar) != numero:
    if adivinhar < numero:
        print('Mais Alto')
    else:
        print('Mais Baixo')
    adivinhar, tentativas = pedir_palpite(tentativas)

print(f'Acertou em {tentativas} tentativas!')
