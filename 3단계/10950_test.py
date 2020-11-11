count = int(input())
allnum = []
allsum = []
print("입력값", count)
for i in range(1, count+1):
    all = input()
    num = all.split()
    allnum = allnum+num
    print(i*2-2, "번째 수")
    print(i*2-1, "번째 수")
    a = int(allnum[i*2-2])
    b = int(allnum[i*2-1])
    sum = a+b
    allsum.append(sum)
    print("합은", a+b)
print(allnum)
print(allsum)

for i in range(1, count+1):
    print(allsum[i-1])
