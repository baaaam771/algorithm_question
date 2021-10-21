arr = []
n = int(input())

for _ in range(n):
    arr.append(list(map(str, input())))

# print(arr)
# print(arr[0])

# ex1 = ['O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O']
# ex1 = ['O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O']
# ex1 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# ex1 = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# ex1 = ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X']
# print(ex1[0])
# print(len(ex1))
score = []
for a in range(n):
    for i in range(len(arr[a])):
        score.append(0)

# print(score)

    for i in range(len(arr[a])):
        if arr[a][i] == 'O':
            if arr[a][i-1] == 'O':
                score[i] = score[i-1]+1
                print(score)
            else:
                score[i] = 1
                print(score)
        else:
            score[i] = 0
            print(score)

    ans = 0
    for i in range(len(arr[a])):
        ans += score[i]

    print(ans)


# score = 0
# s=1
# for i in range(len(ex1)):
#   if ex1[i] == ex1[i+1]:
#     score + s
