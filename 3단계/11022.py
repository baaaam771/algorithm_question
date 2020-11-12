count = int(input())
allnum = []
allsum = []

for i in range(1, count+1):
    all = input()
    num = all.split()
    allnum = allnum+num
    a = int(allnum[i*2-2])
    b = int(allnum[i*2-1])
    sum = a+b
    allsum.append(sum)

for i in range(1, count+1):
    print("Case #%d:" % i, allnum[i*2-2], "+", allnum[i*2-1], "=", allsum[i-1])
