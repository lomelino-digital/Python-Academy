"""Dado um dicionário com nomes de pessoas como chave e a marca das sapatilhas que
cada uma está usando como valor, imprima todas as chaves (nomes) para as sapatilhas
“NIKE”."""


sapatilhas_por_pessoa = {
    "João": "NIKE",
    "Beatriz": "Adidas",
    "Gonçalo": "Puma",
    "Inês": "NIKE",
    "Diogo Oliveira": "Vans",
    "José": "NIKE",
    "Maria": "Puma",
}

for nome, marca in sapatilhas_por_pessoa.items():
    if marca == "NIKE":
        print(nome)

    