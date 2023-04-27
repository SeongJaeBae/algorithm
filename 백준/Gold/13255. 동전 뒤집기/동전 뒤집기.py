n = int(input())
k = int(input())

pr = n
for i in map(int, input().split()):
    tmp = 0
    tmp = tmp + pr * (1 - float(i / n))
    tmp = tmp + (n - pr) * float(i / n)
    pr = tmp
print(pr)