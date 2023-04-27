import sys
from collections import defaultdict
from itertools import permutations
input = sys.stdin.readline

n =int(input())
arr = list(map(int,input().split()))
answer = sorted(arr)
    
def solve(dp, s):
    if s in dp: 
        return dp[s]
    value = 0.0
    arr = list(s)
    n = len(s)
    cnt = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                value+=1
                arr[i],arr[j] = arr[j],arr[i]
                value += solve(dp,tuple(arr))
                arr[i],arr[j] = arr[j],arr[i]
            else:
                cnt +=1
    d = n*(n-1)//2
    dp[s] = value/(d-cnt)
    return dp[s]

dp = {tuple(answer):0.0}
print(solve(dp,tuple(arr)))
