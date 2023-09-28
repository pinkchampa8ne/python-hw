# Write your code here :-)
def g1(x):
    if x > 0:
        y = 2*x - 2
        if y > 0:
            z = x
            while y > 0:
                x = z * 10**y + x
                y = y - 2
            return x
        if y == 0:
            return 1
    if x == 0:
        return 0


print(g1(1))
print(g1(2))
print(g1(3))
print(g1(4))
print(g1(5))
print(g1(6))
print(g1(7))


def g(x):
    if x > 0:
        return 100 * g(x-1) + 1
    if x == 0:
        return 0

def g2(x):
    if x < 2:
        return x
    if x >= 2:
        return g(x) * x

print(g2(0))
print(g2(1))
print(g2(2))
print(g2(3))
print(g2(4))
print(g2(5))
print(g2(6))
print(g2(7))
print(g2(35))
print(g2(123))
