today_is_opposite_day = True

#Set say_it_is_opposite_day based on today_is_opposite_day using purposefully verbose conditions given in the book:
# First realization: if today_is_opposite_day == True:
# is equivalent to if today_is_opposite_day: when the variable is a Boolean.
#
#  == is a comparison operator that returns a Boolean,
# while if x directly evaluates the truth value of x.

if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# Say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day')
