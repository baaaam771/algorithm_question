# a = int(input())

# for i in range(1, 10):
#     print(a, "*", i, "=", a*i)


# def gugu(x):
#     for i in range(1, 10):
#         print(x, "*", i, "=", x*i)


# print(gugu(a))
num = int(input())

for i in range(1, num+1):
    print(" "*(num-i)+"*"*i)
