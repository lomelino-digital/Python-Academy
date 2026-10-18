# Crie um Script que peça o nome e a data de nascimento.
# Exemplo de output: “Olá José, você nasceu no dia 1 de março de 1979"

nome = input("Qual o seu nome?")
data = input("Qual a sua data de nascimento?")

print("Olá {}, você nasceu no dia {}".format(nome,data))