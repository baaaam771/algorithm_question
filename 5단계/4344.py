arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)

for a in range(n):

    add = 0
    for i in range(1, len(arr[a])):
        add += arr[a][i]
        # print(add)

    avg = 0
    avg = add / (len(arr[a])-1)
    # print(len(arr[0])-1)
    # print(avg)

    count = 0

    for i in range(1, len(arr[a])):
        if arr[a][i] > avg:
            count += 1
    # print(count)

    per = count/(len(arr[a])-1)*100
    rou = round(per, 3)
    # print(rou,"%")
    pri = "{:.3f}%".format(rou)
    print(pri)
