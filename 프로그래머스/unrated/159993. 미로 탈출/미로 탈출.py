def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    #상하좌우
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    
    def bfs(x,y,end):
        q = []
        visited = [[-1]*m for _ in range(n)]
        visited[x][y] = 0
        q.append((x,y))
        while(len(q)>0):
            x, y = q.pop(0)
            print(x,y)
            if maps[x][y] == end:
                return [visited[x][y],x,y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == -1:
                        if maps[nx][ny] != 'X':
                            q.append([nx,ny])
                            visited[nx][ny] = visited[x][y] + 1

        return None
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x,y = i,j
                break
    count = bfs(x,y,'L')            
    if count == None:
        print("no L")
        return -1
    answer += count[0]
    count = bfs(count[1],count[2],'E')
    if count == None:
        print("No E")
        return -1
    answer += count[0]
    
    
    return answer