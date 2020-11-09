all = input()
num = all.split()
a = int(num[0])
b = int(num[1])


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x//y


def mod(x, y):
    return x % y


print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))
print(mod(a, b))
