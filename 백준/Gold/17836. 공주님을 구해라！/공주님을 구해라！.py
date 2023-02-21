def bfs():
    global sword
    q = []
    visited[0][0] = 1
    q.append((0,0))
    while(len(q)>0):
        x, y = q.pop(0)
        if(arr[x][y] == 2):
            sword = n-1-x + m-1-y + visited[x][y]-1
        if(x == n-1 and y == m-1):
            return min(visited[x][y]-1, sword)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<n and 0<=ny<m and arr[nx][ny] != 1):
                if(visited[nx][ny] == 0):
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return sword
#상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m, limit = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
sword = 1000000
res = bfs()
# 최단거리를 계산한 값이 제한시간보다 클 경우 실패
print("Fail" if(res>limit) else res)