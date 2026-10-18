while True:
    linf = input('Introduza o limite inferior: ')
    lsup = input('Introduza o limite superior: ')
    try:
        linf = int(linf)
        lsup = int(lsup)
        
        if lsup > linf:
            for i in range (linf,lsup+1):
                print(i)
            break
        else:
            print('Os limites, indicados para o intervalo, estão errados')
            break


    except ValueError:
        print('Introduza dois números inteiros por favor...Tente de novo')
        continue