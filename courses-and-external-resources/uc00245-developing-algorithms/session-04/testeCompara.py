def Compara(a,b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('Erro, não introduziu um número.')
    else:    
        if a == b:
            print('Os números são iguais')
        elif a > b:
            print(f"{a} é maior que {b}")
        else:
            print(f"{b} é maior que {a}")

Compara(input('Introduza primeiro número:'),input('Introduza segundo número:'))
    