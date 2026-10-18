#def commaCode(my_list):
#    codedList=[]
#    for i in range(len(my_list)):
#        if i < (len(my_list)-1):
#            codedList.append(my_list[i])
#        else:
#            codedList.append('and ' + my_list[i])
#    print (codedList)
#    return codedList

#spam = ['apples', 'bananas', 'tofu', 'cats']

#commaCode(spam)

# first try was not it

def commaCode(my_list):
    commaList = ''
    for i in range(len(my_list)):
        if i < (len(my_list)-1):
            commaList+= my_list[i] + ', '
        else:
            commaList+='and ' + my_list[i]
    print(commaList)

spam = ['apples', 'bananas', 'tofu', 'cats']

commaCode(spam)