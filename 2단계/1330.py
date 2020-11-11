all = input()
num = all.split()

a = int(num[0])
b = int(num[1])


def compare(x, y):
    if x > y:
        return ">"
    elif x < y:
        return "<"
    else:
        return "=="


print(compare(a, b))
