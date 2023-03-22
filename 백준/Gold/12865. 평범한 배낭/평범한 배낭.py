import sys

N, K = map(int, input().split())
stuff = [[0,0]]
sack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w= stuff[i][0] 
        v= stuff[i][1]
       
        if j < w:
            sack[i][j] = sack[i - 1][j]
        else:
            sack[i][j] = max(v+ sack[i - 1][j - w], sack[i - 1][j])

print(sack[N][K])