import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m,n = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
#경로의 수
dp = [[-1]*n for _ in range(m)]


def dfs(x, y):
    # 이미 방문한 적이 있을 경우
    if dp[x][y] != -1:
        return dp[x][y]

    # Base case
    if x == m-1 and y == n-1:
        return 1

    # Recursive case
    dp[x][y] = 0

    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]

        if 0 <= nextX <= m-1 and 0 <= nextY <= n-1:
            if arr[x][y] > arr[nextX][nextY]:
                dp[x][y] += dfs(nextX, nextY)

    return dp[x][y]

print(dfs(0, 0))