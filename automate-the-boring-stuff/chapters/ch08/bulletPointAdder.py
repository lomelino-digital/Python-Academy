import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)


"""This is a test
for the bullets adder
using pyperclip to paste this text and 
get a copy of the bulletted text into the
clipboard, how did it work?"""