# Write your code here :-)
def f(x):
    if len(x) == 0:
        return x
    return x[0] + x[0] + f(x[1:])

def g(x):
    if len(x) == 0:  # Jeff's note: lines 8 and 9 are unnecessary.
        return x     # Often (but not always), you'll find that you don't need a base case if you're not using recursion.
    return x + x

print(f('Hello'))
print(g('Hello'))
print(h('Hello'))

# More homework:
#
# f1('Natalie') returns 'Naatttaaaallllliiiiiieeeeeee'
# f2('Natalie') returns 'NaTaLiE'
# f3('Jeff likes Natalie') returns 'Jf ie aai'

def f1a(x):
    if len(x) == 0:
        return x
    return len(x) * x[0] + f1a(x[1:])

def f1(x):
    if len(x) == 0:
        return x
    y = f1a(h(x))
    return h(y)

print(f1a('Natalie'))
print(f1('Natalie'))

def upper_1_char(s):
    if len(s) == 1:
        return s.upper()
    raise RuntimeError('you must call this on a single character')

def f2(x):
    if len(x) == 1:
        return upper_1_char(x)
    if len(x) == 0:
        return x
    if len(x) > 1:
        new = upper_1_char(x[0]) + x[1]
        x = x[2:]
        return new + f2(x)

def f3(x):
    if len(x) == 0:
        return x
    if len(x) > 0:
        new = x[0]
        x = x[2:]
        return new + f3(x)

print(f2('Natalie'))
print(f2('p'))        # does this return the value you would expect?
print(f2(''))
print(f3('Jeff likes Natalie'))

def alternate_caps(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:2] + alternate_caps(s[2:])

print()
print(alternate_caps('Natalie'))
print(alternate_caps('p'))        # does this return the value you would expect?
print(alternate_caps(''))
print(alternate_caps('Jeff likes Natalie'))
print(alternate_caps('JEFF LIKES NATALIE!!!!@'))

def alternate_caps_v2(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:2].lower() + alternate_caps_v2(s[2:])

print()
print(alternate_caps_v2('Natalie'))
print(alternate_caps_v2('p'))        # does this return the value you would expect?
print(alternate_caps_v2(''))
print(alternate_caps_v2('Jeff likes Natalie'))
print(alternate_caps_v2('JEFF LIKES NATALIE!!!!@'))


# New homework for Sep 9:

# triangle1('Natalie') returns nothing, but prints this to the screen:
# Natalie
# atalie
# talie
# alie
# lie
# ie
# e

# triangle2('Natalie') returns nothing, but prints this to the screen:
# Natalie
# Natali
# Natal
# Nata
# Nat
# Na
# N

# triangle3('Natalie') returns nothing, but prints this to the screen:
# Natalie
#  atalie
#   talie
#    alie
#     lie
#      ie
#       e

# square1('Natalie') returns nothing, but prints this to the screen:
# Natalie
# atalieN
# talieNa
# alieNat
# lieNata
# ieNatal
# eNatali

# square2('Natalie') returns nothing, but prints this to the screen:
# Natalie
# eNatali
# ieNatal
# lieNata
# alieNat
# talieNa
# atalieN
