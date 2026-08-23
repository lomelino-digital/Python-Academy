# I immediately thought of the infinite attempts at the password as an issue, as i read chapter 3 i had some ideas
# I wanted to implement in the swordfish2.py program, namely protection from bruteforce attempts and some
# Error or ending messages when the program was closing:

import sys

tryCounter = 0

while True:
    print('Who are you?')
    name = input('>')
    if name!= 'Joe':
        # I tried tryCounter++ it didn't work and couldn't remember tryCounter += 1 which would've looked better
        tryCounter = tryCounter + 1
        print('Sorry %s I serve only Joe!' % (name))
        if tryCounter > 5:
             print('\n Sorry, you have made too many mistakes already, self destruct initiated 5...4...3...2...1....Goodbye!')
             sys.exit()
        continue
    tryCounter = 0
    while True:
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input('>')
        if password != 'swordfish':
            tryCounter = tryCounter + 1
            if tryCounter > 5:
                print('\n Sorry, you have made too many mistakes already, self destruct initiated 5...4...3...2...1....Goodbye!')
                sys.exit()
            continue
        # Upon reviewing i understand now that the elif or even else are redundant and i can simply leave break 
        # as it's either wrong password continue back to the top of the second while or if doesn't happen and break
        # the original attempt had: elif password == 'swordfish':
        break
    break
print('Access granted.')