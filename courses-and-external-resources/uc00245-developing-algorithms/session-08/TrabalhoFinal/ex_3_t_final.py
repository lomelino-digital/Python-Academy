"""Peça ao utilizador um nome de utilizador e uma password. Defina um nome de utilizador ( admin ) e uma password ( 12345 ) pré-definidos. 
Verifique se as credenciais introduzidas correspondem às prédefinidas e imprima se o login foi bem-sucedido ou falhou.

Exemplo de Interação: 
Nome de utilizador: admin 
Password: 12345 

Login bemsucedido!

def introduzir_credenciais():
    utilizador = input('Defina o seu Nome de utilizador: ')
    password = input('Defina a sua password: ')
    return utilizador, password
"""

def login(util,pwd):
    
    tentativas = 0
    while tentativas < 3:
        username = input('Introduza o seu Nome de utilizador: ')
        passw = input('Introduza a sua password: ')
        if username == util and passw == pwd:
            return "\nLogin bemsucedido!"
        tentativas += 1
        print(f"Login falhado, numero de tentativas restantes {3-tentativas}")
    return "\nNão foi possível fazer login, tente de novo daqui a 1 hora."



utilizador, password = 'admin','12345'
print(login(utilizador, password))
