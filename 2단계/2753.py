num = int(input())


def check(i):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        return 1
    else:
        return 0


print(check(num))
