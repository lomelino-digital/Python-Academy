import random
guess = ''
while guess not in ('heads', 'tails'):
    print('guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0,1) # 0 is tails,1 is heads - first bug we need to turn the int into heads or tails
if toss == 0:  # This selector solves the bug
    toss = 'tails'
else:
    toss = 'heads'
if toss == guess:
    print('you got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')