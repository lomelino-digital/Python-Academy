def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')

a()

# def a() is calling functions that are not declared yet, 
# which is fine but when a() is called they have been defined already
# This is an example of last in first out which seems to be important
# when handling data, i hear