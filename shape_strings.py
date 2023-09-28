# Write your code here :-)
def triangle1(x):
    if len(x) == 0:
        print(x)
    if len(x) > 0:
        print(x)
        x = triangle1(x[1:])

triangle1('Natalie')

def triangle2(x):
    if len(x) == 0:
        print(x)
    if len(x) > 0:
        y = len(x)-1
        print(x)
        x = x[0:y]
        triangle2(x)

triangle2('Natalie')

def triangle3(x):
    if len(x) == 0:
        print(x)
    y = len(x) * 2
    z = 1
    print(x)
    while len(x) <= y:
        x = ' ' + x
        print(x[0:z]+x[2*z:])
        z = z + 1
    print('')

triangle3('Natalie')

def square1(x):
    if len(x) == 0:
        print(x)
    y = len(x)
    while y > 0:
        print(x)
        x = x[1:] + x[0]
        y = y-1
    print('')

def square2(x):
    if len(x) == 0:
        print(x)
    y = len(x)
    while y > 0:
        print(x)
        x = x[len(x)-1] + x[0:len(x)-1]
        y = y-1
    print('')

square1('Natalie')
square2('Natalie')

def square1a(x, z=''):
    print(x + z)
    if len(x) > 1:
        square1a(x[1:], z + x[0])

square1a('Natalie')
print()

def square2a(x, z=''):
    print(z + x)
    if len(x) > 1:
        square2a(x[:len(x)-1], x[len(x)-1] + z)

square2a('Natalie')
