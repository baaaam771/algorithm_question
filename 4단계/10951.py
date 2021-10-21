arr = []
while True:
    x, y = map(int, input().split())
    z = x + y
    arr.append(z)
for i in range(0, len(arr)):
    print(arr[i])
