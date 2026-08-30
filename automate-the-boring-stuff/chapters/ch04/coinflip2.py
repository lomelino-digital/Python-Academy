# In this version i want to already make use of try and except to allow user to input
# the number of tosses without breaking the program

import random

number_of_tosses = input('Please select the number of coin tosses: ')

while True:
    number_of_tosses = input('Please select the number of coin tosses: ')
    try:
        for i in range(int(number_of_tosses)):  # Perform 100 coin flips.
            if random.randint(0, 1) == 0:
                print('H', end=' ')
            else:
                print('T', end=' ')
        print()
        print('Try again?')
        continue
    except ValueError:
       print()
       print('Please select an integer number of tosses')
       print()
       continue

