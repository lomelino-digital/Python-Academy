
import math

def perimetro(raio):
    return 2*math.pi*raio

def area(raio):
    return math.pi*raio**2

def volume(raio):
    return (4/3)*math.pi*raio**3


raio = input('Introduza o raio: ')
try:
    raio = float(raio)
    if raio < 0:
        raise ValueError
except ValueError:
    print('Erro: Introduza um número não negativo.')
else:
    print(f"O perimetro é {perimetro(raio)}")
    print(f"A área é {area(raio)}")
    print(f"O volume é {volume(raio)}")
