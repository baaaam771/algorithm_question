num = int(input())


def score(i):
    if 90 <= i <= 100:
        return "A"
    elif 80 <= i < 90:
        return "B"
    elif 70 <= i < 80:
        return "C"
    elif 60 <= i < 70:
        return "D"
    else:
        return "F"


print(score(num))
