import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # The answer to question 15 is in rule 
    # 2. A variable in a function with a `global` statement is always a global variable in that function.
    # if we add the local scope variable, notrandomdice.py becomes a randomdice becase of rule
    # 3. Otherwise, if a function uses a variable in an assignment statement, it is a local variable.
    
    # one can just remove the # from the next line to transform the notrandomdice into an actual random dice
    # random_number = random.randint(1, 6)


    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
