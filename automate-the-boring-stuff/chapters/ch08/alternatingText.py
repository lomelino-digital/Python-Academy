import pyperclip

text = pyperclip.paste()
alt_text = ''
make_uppercase = False
for character in text:
    if make_uppercase:
        alt_text += character.upper()
    else:
        alt_text += character.lower()

    make_uppercase = not make_uppercase

pyperclip.copy(alt_text)
print(alt_text)



# Test copy this text to test the programs output, it should come out all upper lower