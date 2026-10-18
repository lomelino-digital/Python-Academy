numero = float(input('Digite um numero real: '))
subtotal = 0
total_n = 0
while numero != 0:
    subtotal += numero
    print(f"Subtotal = {subtotal}")
    numero = float(input('Digite um numero real: '))
    total_n +=1

media = subtotal / total_n
print(f"Total Final = {subtotal}")
print(f"Media = {media}")