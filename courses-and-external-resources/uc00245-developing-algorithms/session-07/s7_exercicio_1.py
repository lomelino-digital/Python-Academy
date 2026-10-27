"""Crie um dicionário chamado livro que represente as informações de um livro com as
seguintes chaves e valores:
"titulo": "O Guia do Mochileiro das Galáxias"
"autor": "Douglas Adams"
"ano": 1979
"paginas": 224
Imprima o valor associado à chave "autor".
Adicione uma nova chave-valor: "genero": "Ficção Científica".
Altere o valor da chave "ano" para 1980.
Imprima o dicionário completo."""


livro = {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "ano": 1979, "paginas": 224,}
print(livro["autor"])
livro["genero"] = "Ficção Científica"
livro["ano"] = 1980
print(livro)