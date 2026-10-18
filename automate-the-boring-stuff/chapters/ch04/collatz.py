def collatz(number):
    if number % 2 == 0:
        # original code, mistakenly tried to write the less lines of code
        # when checking for improvements i learned we're better of optimizing
        # to avoid repeated operations and save the calculation when running it
        # more than once, the more correct code would be:
        # collatz_number = number // 2
        # print(collatz_number, end=' ')
        # return collatz_number
        #
        # And similar structure for the else

        print(number // 2, end=' ') 
        return number // 2      
        
    else:
        print(3 * number + 1, end=' ')
        return (3 * number + 1)


while True:
    starting_number = input('Please select the integer to collatz: ')
    try:
        starting_number = int(starting_number)
        while starting_number != 1:         
            starting_number = collatz(starting_number)
    except ValueError:
        print('You did not select an integer to collatz, you must select an integer in order for me to collatz \n')
        continue
    print('\n\n One more time\n')