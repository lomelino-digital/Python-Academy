"""A Short Program: Pig Latin

Pig latin is a silly made-up language that alters English words. 
If a word begins with a vowel, the word yay is added to the end of it. 
If a word begins with a consonant or consonant cluster (like ch or gr), 
that consonant or consonant cluster is moved to the end of the word and followed by ay."""

def message_intake():
    message = ''
    while len(message) == 0:
        print('Write a non-empty message in English to be translated into pig latin: ')
        message = input()
    return message

VOWELS = ['a','e','i','o','u','y']

pig_latin = []

message = message_intake()
message_list = message.split()




for word in message_list:
    if word.isalpha():
        if word[0].lower() in VOWELS:
            pig_latin.append(word + 'yay')     
        else:
            pig_latin.append(word[1:]+word[0]+'ay')
    if not word.isalpha():
        for i in range(len(word)-1,-1,-1):
 
            if not word[i].isalpha() and word[(i-1)].isalpha():
                if word[0].lower() in VOWELS:
                    pig_latin.append(word[:i] + 'yay' + word[i:])     
                elif not word[0].lower() in VOWELS:
                    pig_latin.append(word[1:i]+word[0]+'ay'+word[i:])
            elif all(not char.isalpha() for char in word):
                pig_latin.append(word)
                break


            


new_message = " ".join(pig_latin)

print(new_message)


