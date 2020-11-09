all = input()
num = all.split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

i = (a+b) % c
j = ((a % c)+(b % c)) % c
k = (a*b) % c
l = ((a % c)*(b % c)) % c

print(i)
print(j)
print(k)
print(l)
