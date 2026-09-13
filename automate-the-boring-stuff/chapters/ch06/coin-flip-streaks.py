import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run the experiment 10000 times total.
    each_experiment = []
    for i in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            each_experiment.append('H')
        elif flip == 1:
            each_experiment.append('T')

    for i in range(95):
            if each_experiment[i] == 'H':
                for j in range(6):
                    if each_experiment[i+j] != 'H':
                        break
                else:
                    number_of_streaks += 1
                    break
            elif each_experiment[i] == 'T':
                for j in range(6):
                    if each_experiment[i+j] != 'T':
                        break
                else:
                    number_of_streaks += 1
                    break
# I was making it harder, wanted to count how many streaks of 6 in each 100 flip
print('number of 100 flips containing a streak: ' + str(number_of_streaks))
percent_flips = (number_of_streaks/10000) * 100               
print()
print('percentage of 100 flips that contain a 6 streak: ' + str(percent_flips) + '%')
        