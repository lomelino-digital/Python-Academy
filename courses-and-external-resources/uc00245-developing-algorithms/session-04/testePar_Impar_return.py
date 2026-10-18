# Crie uma função Par_Impar, que verifique se o número inserido é par ou ímpar. Execute no ficheiro testePar_Impar.py

def Par_Impar(numero):
    try:
        numero = float(numero)
        if  numero != int(numero):
            raise ValueError
    except ValueError:
        return 'Não introduziu um número inteiro'
    if numero % 2 == 0:
        return 'Número Par'
    else:
        return 'Número Impar'


print(
    Par_Impar(input('Introduza um número: ')) )

