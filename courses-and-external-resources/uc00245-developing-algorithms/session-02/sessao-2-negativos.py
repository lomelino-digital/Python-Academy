valor = int(input('valor: '))

match valor:
    case valor if valor < 0:
        print('Valor Negativo')
    case valor if valor > 0:
            print('Valor Positivo')
    case 0:
        print('Valor é 0')