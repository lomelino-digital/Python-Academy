numero = 1

for i in range(1,6):
    linha=[]
    for j in range(i):
        linha.append(str(numero))
        numero += 1
    print(" ".join(linha))