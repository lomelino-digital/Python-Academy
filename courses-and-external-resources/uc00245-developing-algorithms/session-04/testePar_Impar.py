# Crie uma função Par_Impar, que verifique se o número inserido é par ou ímpar. Execute no ficheiro testePar_Impar.py

def Par_Impar(numero):
    try:
        numero = float(numero)
        if  numero != int(numero):
            raise ValueError
    except ValueError:
        print('Não introduziu um número inteiro')    

    else:
        if numero % 2 == 0:
            print('Número Par')
        else:
            print('Número Impar')   


Par_Impar(input('Introduza um número: ')) 