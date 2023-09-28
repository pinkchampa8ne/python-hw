def f(x):
    if x > 0:
        return 100 * f(x-1) + x
    if x == 0:
        return 0

def g(x):
    if x > 0:
        return 100 * g(x-1) + 5
    if x == 0:
        return 0

def h(x):
    if x > 0:
        return 2*h(x-1)
    if x == 0:
        return 1

print(f(1))
print(f(2))
print(f(5))

print(g(1))
print(g(2))
print(g(5))

print(h(0))
print(h(1))
print(h(2))
print(h(3))
