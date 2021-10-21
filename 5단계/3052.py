arr = []
for _ in range(10):
    arr.append(int(input()))

# print(arr)
last = []
for i in range(10):
    n = arr[i] % 42
    last.append(n)

# print(last)

print(len(list(set(last))))
