"""Criar uma função que recebe uma lista de palavras e uma letra.
Devolve apenas as palavras que começam com essa letra (sem distinção de maiúsculas/minúsculas)."""

def palavras_que_comecam_por(palavras,letra):
    nova_lista = []
    for word in palavras.split():
        if word[0].lower() == letra.lower():
            nova_lista.append(word)
    return nova_lista


def pedir_palavras():
    while True:
        palavras = input('Introduza uma lista de palavras: ')
        palavras2 = palavras.split()
        for word in palavras2:
            if not word[0].isalpha():
                print("Apenas palavras começadas por letras.")
                break
        else:
            return palavras



def pedir_letra():
    while True:
        letra = input('Introduza a inicial das palavras que pretende: ')
        if not letra.isalpha():
            print("Apenas palavras começadas por letras.")
        else:
            if letra == 'ç':
                letra = 'c'
            return letra




lista = pedir_palavras()
letra = pedir_letra()

if len(palavras_que_comecam_por(lista,letra)) > 0:
    print(f"\nlista de palavras: {palavras_que_comecam_por(lista,letra)}\n")
    print(f'A frase das palavras que começam por {letra} é: {" ".join(palavras_que_comecam_por(lista,letra))}')
else:
    print(f"Nenhuma palavra começa por {letra}")        

