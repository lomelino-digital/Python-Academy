
vogais_pt = (
    'A', 'Á', 'À', 'Â', 'Ã',
    'E', 'É', 'È', 'Ê', 'Ẽ',
    'I', 'Í', 'Ì', 'Î', 'Ĩ',
    'O', 'Ó', 'Ò', 'Ô', 'Õ',
    'U', 'Ú', 'Ù', 'Û', 'Ũ','Y'
)


mensagem = input('Introduza a mensagem a transformar: ')
nova_mensagem = []

for word in mensagem.split():    
    new_word = []
    for letra in word:
        if letra.upper() in vogais_pt:
            letra = '*'

        new_word.append(letra)
    nova_mensagem.append("".join(new_word))


print(" ".join(nova_mensagem))