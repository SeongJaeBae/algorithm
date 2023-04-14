import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def main():
    def make_holes():
        K = int(input())
        for _ in range(K):
            i, j = map(int, input().split())
            dp[i][j] = 0

    def find_dp(i, j):
        if dp[i][j] != -1: return dp[i][j]
        val = find_dp(i-1, j)+find_dp(i, j-1)
        val += find_dp(i-1, j-1) if j%2 else find_dp(i+1, j-1)
        dp[i][j] = int(val%X)
        return dp[i][j]

    X = 1e9+7
    I, J = map(int, input().split())
    dp = [[-1]*(J+1) for _ in range(I+2)]
    dp[1][1] = 1
    for i in range(I+1):
        dp[i][0] = 0
    for j in range(J+1):
        dp[0][j] = 0
        dp[I+1][j] = 0
    make_holes()
    return find_dp(I, J)

print(main())