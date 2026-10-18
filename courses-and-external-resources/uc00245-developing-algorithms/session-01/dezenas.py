numero = input('introduza um número inteiro: ')
try:
    print('O dígito das dezenas é: ',numero[-2])
except IndexError:
    print('O dígito das dezenas é:', 0)