all = input()
num = all.split()

a = int(num[0])
b = int(num[1])


def alarm(x, y):
    if y < 45:
        x -= 1
        y += 60
    if x == -1:
        x += 24
    y -= 45
    return x, y


print(alarm(a, b)[0], alarm(a, b)[1])
