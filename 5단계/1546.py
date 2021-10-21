n = int(input())
arr = []
nums = list(map(int, input().split()))
high = max(nums)

score = []
for i in range(n):
    s = nums[i]/high*100
    score.append(s)

# print(score)

ans = 0
for i in range(n):
    ans += score[i]

# print(ans)
print(ans/n)
