num = int(input())
list = []
for i in range(1, num+1):
    list.append(i)

list.reverse()

for i in range(1, num+1):
    print(list[i-1])
