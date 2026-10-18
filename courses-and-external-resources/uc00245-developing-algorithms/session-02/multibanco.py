def notas(levantamento):
    notas_200, notas_100, notas_50, notas_20, notas_10, notas_5 = 0,0,0,0,0,0


    while levantamento > 0:
        if levantamento >= 200:
            notas_200 += 1
            levantamento -=200
        elif levantamento >= 100:
            notas_100 += 1
            levantamento -=100
        elif levantamento >= 50:
            notas_50 += 1
            levantamento -=50
        elif levantamento >= 20:
            notas_20 += 1
            levantamento -=20
        elif levantamento >= 10:
            notas_10 += 1
            levantamento -=10
        elif levantamento >= 5:
            notas_5 += 1
            levantamento -=5
    return notas_200, notas_100, notas_50, notas_20, notas_10, notas_5

while True:
    valor = input('Qual o valor que pretende levantar? >')
    try:
        valor = int(valor)
        if valor < 10 or valor > 400:
            print('Valor de levantamento inválido, Introduza um número entre 10 e 400.', end='\n ---------------------------------------------------------------\n')
            continue
        elif valor % 5 != 0:
            print('Valor de levantamento inválido, A nota mais pequena é de 5', end='\n ---------------------------------------------------------------\n')
            continue
        else:
            dist_notas = notas(valor)

            print(f"{dist_notas[0]} nota de 200€")  
            print(f"{dist_notas[1]} nota de 100€") 
            print(f"{dist_notas[2]} nota de 50€")
            print(f"{dist_notas[3]} nota de 20€")
            print(f"{dist_notas[4]} nota de 10€")
            print(f"{dist_notas[5]} nota de 5€")
                      
            break
    except ValueError:
        print('Valor inválido. Selecione um número inteiro.',end='\n ---------------------------------------------------------------\n')
        
        continue