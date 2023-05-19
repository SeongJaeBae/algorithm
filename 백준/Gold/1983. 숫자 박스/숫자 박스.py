import sys
import math
input = sys.stdin.readline

n = int(input())

arr = [[], []]
cnt1 = 0
cnt2 = 0
arr = [[], []]
for i in range(2):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)
    for j in temp:
        if j:
            if not i:
                arr[0].append(j)
                cnt1 += 1
            else:
                arr[1].append(j)
                cnt2 += 1


dp = [[[-9876543210] * n for _ in range(cnt2)] for _ in range(cnt1)]
def solve(i,j,k):
    if i == cnt1 or j == cnt2:
        return 0
    if dp[i][j][k] != -9876543210:
        return dp[i][j][k]
    if cnt1 - i + k < n:
        dp[i][j][k] = max(dp[i][j][k], solve(i, j + 1, k + 1))
    if cnt2 - j + k < n:
        dp[i][j][k] = max(dp[i][j][k], solve(i + 1, j, k + 1))
    dp[i][j][k] = max(dp[i][j][k], arr[0][i] * arr[1][j] + solve(i + 1, j + 1, k + 1))
    return dp[i][j][k]

print(solve(0,0,0))