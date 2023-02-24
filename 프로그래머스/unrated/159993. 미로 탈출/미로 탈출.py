from collections import deque

def solution(maps):
    answer = 0
    x_len = len(maps[0])
    y_len = len(maps)
    visit = [[0]*x_len for _ in range(y_len)]
    
    for i in range(y_len) :
        for j in range(x_len) :
            if maps[i][j] == "S" :
                Sx, Sy = j, i
            if maps[i][j] == "E" :
                Ex, Ey = j, i
            if maps[i][j] == "L" :
                Lx, Ly = j, i
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    def bfs(x,y) :
        q = deque()
        q.append((x,y))
        
        while q :
            x, y = q.popleft()
            
            for i in range(4) :
                px = dx[i] + x
                py = dy[i] + y
                
                if 0<=px<x_len and 0<=py<y_len :
                    if visit[py][px] == 0 and maps[py][px] != "X" :
                        visit[py][px] = visit[y][x] + 1 
                        q.append((px,py))
    
    bfs(Sx,Sy)
    answer += visit[Ly][Lx]
    
    visit = [[0]*x_len for _ in range(y_len)]
    
    bfs(Lx,Ly)
    answer += visit[Ey][Ex]
    
    if visit[Ey][Ex] == 0 or visit[Ly][Lx] == 0 or visit[Sy][Sx] == 0: 
        return -1
    
    return answer