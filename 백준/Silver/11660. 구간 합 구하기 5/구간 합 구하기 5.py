import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int,input().split())) for i in range(n)]
target = [list(map(int,input().split())) for i in range(m)]

prefix_sum = [[0] * (n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = data[i-1][j-1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for x1, y1, x2, y2 in target:
    tmp = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(tmp)