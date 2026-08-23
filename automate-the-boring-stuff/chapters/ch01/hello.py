print('Hello, world!')
print('What is your name?')  #Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') #Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age)+1) + ' in a year.')

# In case we think the user may insert a decimal number as the answer to the age question we could write:
#print('You will be ' + str((int(float(my_age))) + 1)+ ' in a year.')
