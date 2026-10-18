def Compara(a,b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return 'Erro, não introduziu um número.'   
    if a == b:
        return 'Os números são iguais'
    elif a > b:
        return f"{a} é maior que {b}"
    else:
        return f"{b} é maior que {a}"

print ( Compara(
    input('Introduza primeiro número:'),
    input('Introduza segundo número:')
    ))

    