import random, sys, time
WIDTH = 70 # The number of columns

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # Should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Loop over each column:
        for i in range(WIDTH):
            if random.random()<0.02:
                # Restart a stream counter on this column if a randomly generated float between 0 and 1 is < 0.02   ie: 2% of the times
                # The tream length is between 4 and 14 characters long:
                columns[i] = random.randint(4,14)

                # print a character in this column:
            if columns[i] == 0:
                print(' ',end='')
            else:
                # print a 0 or 1:
                print(random.choice([0,1]), end='')
                # This raised some questions and the option seems to come from convention or habit, from what i understand
                # there are some choices that are simpler and more compute efficient, some choices to test:
                # print(random.randint(0,1), end='')
                # print(random.getrandbits(1), end='')
                
                # They tested well

                columns[i] -= 1  # decrement character counter for this column i

        print() # print a new line at the end of every row
        time.sleep(0.1)  # Each row pauses for one tenth of a second.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

