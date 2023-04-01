import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
li = list(map(int,input().split()))
m = int(input())
d = defaultdict(list)

for i in range(n):
    if i == m:
        continue
    d[li[i]].append(i)

def dfs(index):
    if d[index] == []:
        return 1
    num = 0
    for i in d[index]:
        num += dfs(i)
    return num

if d[-1]==[]:
    print(0)
else:
    print(dfs(-1))