while True:
    numero_solicitado = int(input('Introduza um número inteiro positivo: '))
    i = numero_solicitado
    if numero_solicitado < 1:
        print('numero inferior a 1!')
        
        continue
    else:
        while i >= 1:  # Com while
            print(i)
            i -= 1

        for i in range (numero_solicitado,1,-1): # Com for
            print(i)
        break
