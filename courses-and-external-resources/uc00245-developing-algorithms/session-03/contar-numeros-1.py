

while True:
    numero_solicitado = int(input('Introduza um número inteiro positivo: '))
    i = 1
    if numero_solicitado < 1:
        print('numero inferior a 1!')
        
        continue
    else:
        while i <= numero_solicitado: # Com while
            print(i)
            i += 1

        for i in range (1,numero_solicitado+1): # Com for
            print(i)
        break