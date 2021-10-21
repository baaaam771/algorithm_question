import sys
r = int(input())
arr = []
for _ in range(1, r+1):
    a, b = map(int, sys.stdin.readline().split())
    c = a + b
    arr.append(c)
for i in range(0, len(arr)):
    print(arr[i])
