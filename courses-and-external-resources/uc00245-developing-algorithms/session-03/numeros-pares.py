while True:
    numero_inicial = input('Introduza o número inicial: ')
    numero_final = input('Introduza o número final: ')
    try:
        numero_inicial = int(numero_inicial)
        numero_final = int(numero_final)
        quantidade = 0
        if numero_inicial > 0 and numero_final > 0 and numero_final > numero_inicial:
            for i in range (numero_inicial,numero_final+1):
                if i % 2 == 0:
                    print(i)
                    quantidade +=1
        else:
            print('Tente de novo\n')
            continue

        print(f"Quantidade: {quantidade}")
        break
    except ValueError:
        print('Introduza dois números inteiros por favor...Tente de novo')
        continue