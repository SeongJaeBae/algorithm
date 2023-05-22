import sys
import math
input = sys.stdin.readline

n,l = map(int,input().split())
answer =0

water = [list(map(int,input().split())) for _ in range(n)]

water.sort()
j = 0
for s,e in water:
    s = max(j,s)
    tmp = math.ceil((e-s)/l)
    answer += tmp
    j = s+ tmp*l
print(answer)