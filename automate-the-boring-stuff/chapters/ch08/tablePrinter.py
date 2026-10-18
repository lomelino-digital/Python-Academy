# Function that takes a list of strings and displays them in an ordganized table
# with right justfied columns


def printTable(table_to_print):
    width = find_width(table_to_print)
    rows = find_number_of_rows(table_to_print)
    row = 0
    while row < int(rows):
        for column in table_to_print:
            print(str(column[row]).rjust(width[table_to_print.index(column)]),end=' ')
            
        row += 1
        print()




def find_number_of_rows(table_to_print):
    column_size = [len(column) for column in table_to_print]
    if len(column_size) > 0:        
        return max(column_size)
    return 0



def find_width(table_to_print):
    width = []   
    for column in table_to_print:
        row = [len(str(item)) for item in column]
        width.append(max((row)))
    return width




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],]



# printTable(tableData)


# Two tests that fail - The v2 upgrade of the program will be a later project

# test 1: smallest possible table
# tableData = [['a']]
# output(as intended):
# a (desired output)

# test 2: one column, three rows
# tableData = [['apples', 'oranges', 'cherries']]
# output(as intended):
#   apples 
#  oranges 
# cherries

# test 3: two identical columns
# tableData = [['a', 'b'], ['a', 'b']]
# output(as intended):
# a a 
# b b 

# test 4: numbers inside a column
# tableData = [['a', 'b'], [1, 22]]
# output(as intended):
# a  1 
# b 22 

# test 5: columns of different lengths
# tableData = [['a', 'b', 'c'], ['x']]
# 
#  File "/home/alexandre/Desktop/MPC/Python Learning/Python Academy/automate-the-boring-stuff/chapters/ch08/tablePrinter.py", line 11, in printTable
#    print(str(column[row]).rjust(width[table_to_print.index(column)]),end=' ')
#              ~~~~~~^^^^^
# IndexError: list index out of range

# test 6: empty table
# tableData = []
# returns nothing (correctly)

# test 7: one empty column
# tableData = [[], ['a']]
#  line 31, in find_width
#    width.append(max((row)))
#                 ~~~^^^^^^^
# ValueError: max() iterable argument is empty

# test 8: empty strings as items
#tableData = [['', ''], ['x', 'y']]
# output(as intended):
# x 
# y 


printTable(tableData)