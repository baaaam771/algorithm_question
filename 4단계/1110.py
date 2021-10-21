# print(27%10)
# print(27//10)
count = 0
a = 0
b = 100
c = 100
n = int(input())
# print("n :",n)

a = n

x = a//10
y = a % 10
# print(n, x, y)

add = x+y
new = y*10 + add % 10
# print(new)

b = new
count = 1

c = b

while n != b:
    # for _ in range(0,10):
    a = c
    x = a//10
    y = a % 10
    # print(n, x, y)

    add = x+y
    new = y*10 + add % 10
    # print(new)

    b = new
    count += 1
    # print("a :",a)
    # print("b :",b)
    # print("count :",count)
    c = b
    # a = c

print(count)
