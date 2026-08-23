print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit =='tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

# Adding an exit message in case the user does not give one of the expected results, using the exit()
# function which is outside the materials but purposefully won't look for a way
# to loop back to the beginning, my gets tells me while but i'm not in that chapter yet    
else:
    print('Enter TB or GB for the advertised unit, please use all UPPERCASE or lowercase next time:')
    exit()

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundreths,
# and convert it to a string so it can be concatenated
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)
    
