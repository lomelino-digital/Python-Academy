"""
    1. Realize um programa utilizando a biblioteca MATH e pedindo o valor do RAIO, que permita calcular:
        a. O Perímetro da Circunferência (P = 2*Pi x R)
        b. A área da Circunferência (A = PixR^2)
        c. O Volume da Esfera (V =(4xPixR^3)/3 )"""


import math



def perimetro(raio):
    try:
        raio = float(raio)
        if raio < 0:
            raise ValueError
    except ValueError:
        return 'Erro: Introduza um número não negativo.'
    return 2*math.pi*raio

def area(raio):
    try:
        raio = float(raio)
        if raio < 0:
            raise ValueError
    except ValueError:
        return 'Erro: Introduza um número não negativo.'
    return math.pi*raio**2

def volume(raio):
    try:
        raio = float(raio)
        if raio < 0:
            raise ValueError
    except ValueError:
        return 'Erro: Introduza um número não negativo.'
    return (4/3)*math.pi*raio**3

radius = input('Introduza o raio: ')

print(f"O perimetro é {perimetro(radius)}")
print(f"A área é {area(radius)}")
print(f"O volume é {volume(radius)}")
