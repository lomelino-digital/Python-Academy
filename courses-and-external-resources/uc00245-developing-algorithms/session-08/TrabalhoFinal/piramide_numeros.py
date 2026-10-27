def receber_altura():
    while True:
        alt = input('Introduza a altura do triangulo de numeros: ')
        if alt.isdecimal():
            return int(alt)
        print("\nIntroduza um número inteiro:")

altura = receber_altura()
numero = 1

for row in range(1,altura+1):
    linha=[]
    for i in range(row):
        linha.append(str(numero))
        numero += 1
    print(" ".join(linha))