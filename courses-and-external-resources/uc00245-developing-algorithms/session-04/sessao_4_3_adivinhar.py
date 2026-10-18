"""Crie um jogo que gere um nº aleatório entre 0 e 10 peça ao utilizador que pense num número entre o mesmo intervalo. 
O programa, à medida que o utilizador vai inserindo valores, vão sendo guardadas as tentativas. 
Quando o utilizador acertar no número, deverá surgir “Acertou!!” e em quantas tentativas foi."""

import random

numero = random.randint(0,10)
tentativas = 0

while True:
    tentativas += 1
    adivinhar = input('Adivinhe o número: ')
    try:
        adivinhar = int(adivinhar)
        if not (0 <= adivinhar <= 10):
            raise ValueError
    except ValueError:        
        print('Escolha inválida, escolha um número inteiro entre 0 e 10')
        continue
    else:
        if adivinhar == numero:
            print('Acertou!!')
            break
        else:
            print('Escolha incorrecta, tente novamente.')
            continue

print(f'Acertou em {tentativas} tentativas')
