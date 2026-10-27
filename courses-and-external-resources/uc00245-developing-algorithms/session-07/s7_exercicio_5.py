"""Crie um programa que calcula o salário de um funcionário. O salário deve
ser calculado com base no salário base, nas horas extras e nos descontos.
O programa deve usar exceções para lidar com entradas inválidas.
Para calcular o salário, iremos utilizar a seguinte fórmula:
salário = salário_base + (horas_extra * valor_hora) - (descontos * 100)/100
Onde:
● salário_base é o salário base do funcionário;
● horas_extras é o número de horas extras trabalhadas pelo funcionário;
● valor_hora é o valor da hora extra;
● descontos é o valor dos descontos aplicados ao salário.
Pode utilizar o ValueError e/ou TypeError para gerir as excepções de dados inseridos
inválidos."""


def introduzir_numero():
    while True:
        print('Introduza um número:')
        numero = input()
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('Não introduziu um número')

def introduzir_inteiro():
    while True:
        print('\nApenas aceita números inteiros')
        numero = introduzir_numero()
        if numero.is_integer():
            return int(numero)
        print('Não introduziu um número inteiro.\n')


print("Qual o salário base?")
salario_base = introduzir_inteiro()
valor_hora_extra = 1.5 * salario_base/160
print("\nQual o número de horas extra trabalhadas?")
horas_extra = introduzir_numero()
print("\nQual a percentagem de descontos?")
descontos = introduzir_inteiro()

salario = salario_base + (horas_extra * valor_hora_extra)
salario -= salario * descontos /100

print(f"Salário é {salario} Euros")



        
