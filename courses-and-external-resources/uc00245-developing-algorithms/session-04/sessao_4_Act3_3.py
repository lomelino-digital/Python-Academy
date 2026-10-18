"""    3. Crie um programa que faça gerar uma Tupla de 5 números aleatórios. 
        a. Apresente os números gerados. 
        b. Indique o maior e menor número gerado na Tupla
        c. Defina o intervalo de valores gerados ao seu gosto (se possível peça ao utilizador que indique esse intervalo).*"""
import random

# tupla_5 = tuple(random.randint(0,100) for x in range(5))




tupla_5 = random.sample(range(100),5)
print(tupla_5)
print(f"O valor máximo é {max(tupla_5)}")
print(f"O valor minimo é {min(tupla_5)}")