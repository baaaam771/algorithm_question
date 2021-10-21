n, x = map(int, input().split())

# print(n, x)

# arr = []
# arr.append(list(map(int, input().split())))
# print(arr)
arr = list(map(int, input().split()))
# print(arr)
low = []

for i in range(1, n+1):
    num = arr[i-1]
    if num-x < 0:
        # print("low")
        low.append(num)
        # print(low)
    # else :
        # print("high")

print(*low)
# print(arr)
# import sys
# n, x = map(int(sys.stdin.readline().split())

# data = []
# data.append(list(map(int, sys.stdin.readline().split())))
