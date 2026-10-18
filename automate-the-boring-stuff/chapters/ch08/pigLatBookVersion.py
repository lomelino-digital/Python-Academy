# English to piglatin translator as written in automate the boring stuffs chapter 8 with my commentary

print("Enter the English message to translate to pig latin.")
message = input()

VOWELS = ('a', 'e', 'i','o','u','y')    # Tuple created to check for vowels

pig_latin = []    # List to append the pig latin words to

for word in message.split():
    prefix_non_letters = ""
    while len(word) > 0 and not word [0].isalpha():     # For when the word is not a word like '!!!' the cycle will check each character 
        prefix_non_letters += word[0]                   # from the start of the word and update it one by one, this was one of the biggest
        word = word[1:]                                     # challenges i had in my own version of the program, i was a bit shy about modifying word
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue                                        # to send us back to the for as soon as the modified word has no more characters, this closes the
                                                        # way to tackle words that are not words (numbers and !!! type inputs)                                                
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters      # For the regular punctuation (or numbers) at the end of the word
        word = word[:-1]

    was_upper = word.isupper()                                  # Variables to remember the formatting of the word, uppercase or title
    was_title = word.istitle()

    word = word.lower()                                         # Turn the word into lowercase for translation, here i was cyclically checking
                                                                # word[0].lower() in my program which is probably less efficient
    
    # Separating the consonants and transforming word before appending instead of running the translation inside of the append argument
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]                                     # the consonant that goes in the end is not stored in prefix_consonants which can be used as
                                                            # a condition and an element to transform the final word

    if prefix_consonants != '':                             # if the previous while didn't run, ie if word starts with a consonant
        word += prefix_consonants + 'ay'                    # Consonant transform
    else:                                                   # else:
        word += 'yay'                                       # Vowel transform --- at the elements starting with a not alpha character were filtered in 
                                                            # the first while/continue


    # Setting the word back to its case, something i didn't tackle as i was having trouble with the 
    # more structural issues of the program and i found this one to be more cosmetic

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    pig_latin.append(prefix_non_letters + word + suffix_non_letters)  # Now the program appends, after treating all the text data instead of having 
                                                                      # A bunch of different append arguments for each condition.
                                                                      # The book's solution seems less complex with less nested if/elifs and is 
                                                                      # easier to understand.


print(' '.join(pig_latin))

""" Summary of what I noticed after trying to build this program and now copying the book version:

   - The selector len(word) > 0 and transforming word rather than running indexes through the word and slicing the word at each cycle.
   - More usage of supporting variables even though message.split() was not saved as a variable which had been my first choice.
   - The program built did not split into functions but it probably could and that should be my challenge when rewriting the program again since srp
   seems to be the way to build more modular reusable code.
   - Upon testing the program fails to separate 2 words if the user writes without a space between a comma and a word for example - test,this gives est,thistay
   - A new rewrite of the program should capture the simplicity of the solution, make use of supporting variables for it and avoid unnecessary nest
   and cycling through indexes, it should produce functions that I may use later in other projects as transforming a sentence depending on its
   starting character may be something of use.
   - 
"""