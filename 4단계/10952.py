
print("Input two number")
x, y = map(int, input().split())
# print(x, y)
add = []
while x and y != 0:

    z = x+y
    print(z)
    add.append(z)
    print(add)
    print("Initialize x, y and input another two number")
    x, y = map(int, input().split())

print('end')
print(len(add))
for i in range(0, len(add)):
    print(add[i])

    # add.append(z)
    # print(add)
    # if x & y == 0:
    #   print('end')
    #   break
