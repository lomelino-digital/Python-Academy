# Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, and 
# prints Greetings! if anything else is stored in spam.

# Giving the use a chance to input spam for some easter egg greeting
print('Spam?')
spam = input('>')

if spam == 'Yes' or spam == 'yes':
    spam = 1
elif spam == 'No' or spam == 'no':
    spam = 2

# Now that we know if spam stores 1, 2 or something else we can provide the output required in the exercise
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')