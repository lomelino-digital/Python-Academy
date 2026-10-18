def notas(levantamento):
    notinhas = [200, 100, 50, 20, 10, 5]
    distribuicao = {}

    for nota in notinhas:
        numero_de_notas = levantamento // nota
        distribuicao[nota] = numero_de_notas
        levantamento %= nota


    return distribuicao

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

            for nota,numero_de_notas in dist_notas.items():
                if numero_de_notas > 0:
                    print(f"{numero_de_notas} notas de {nota}")
                      
            break
    except ValueError:
        print('Valor inválido. Selecione um número inteiro.',end='\n ---------------------------------------------------------------\n')
        
        continue