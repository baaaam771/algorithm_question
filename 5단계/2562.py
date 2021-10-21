arr = []
for _ in range(9):
    arr.append(int(input()))

# print(arr)
max_num = max(arr)
idx = arr.index(max_num)
print(max_num)
print(idx+1)
