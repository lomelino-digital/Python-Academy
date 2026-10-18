
altura = int(input('Qual a altura do objecto: '))   # No exercicio altura é 7

n_espaços = int((altura - 1)/2)

for i in range(n_espaços+1):
    n_estrelas = altura - (2*(n_espaços-i))
    print(" "*(n_espaços-i),end="")
    print("*"*n_estrelas,end="")
    print(" "*(n_espaços-i))
for i in range(n_espaços-1,-1,-1):
    n_estrelas = altura - (2*(n_espaços-i))
    print(" "*(n_espaços-i),end="")
    print("*"*n_estrelas,end="")
    print(" "*(n_espaços-i))

