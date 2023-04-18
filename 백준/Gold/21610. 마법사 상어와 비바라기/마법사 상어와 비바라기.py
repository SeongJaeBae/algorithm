import sys

input = sys.stdin.readline

n ,m = map(int,input().split())
data = [list(map(int,input().split())) for i in range(n)]
order = [list(map(int,input().split())) for i in range(m)]


def check_move(d,s,x,y,n):
    #좌,좌상,상,우상,우,우하,하,좌하
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    
    nx = (dx[d-1] * s + x)%n
    ny = (dy[d-1] * s + y)%n
    
    return nx,ny


cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
#대각선 체크
dx = [-1,-1,1,1]
dy = [-1,1,-1,1]

for d,s in order:

    #이동 + 해당 위치 물 더해주기
    #대각선 체크해서 물복사 + 해주기
    #다음 구름 생성
    visited = [[False] * n for _ in range(n)]
    bug = []
    for i,j in cloud:
        nx,ny = check_move(d,s,i,j,n)
        bug.append([nx,ny])
        data[nx][ny] += 1
        visited[nx][ny] = True
    

    for x,y in bug:
        tmp =0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<= nx <n and 0<= ny < n:
                if data[nx][ny] >0:
                    tmp +=1
        data[x][y] += tmp


    tmp_cloud = []

    #구름 생성
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and data[i][j] >=2 :
                data[i][j] -= 2
                tmp_cloud.append([i,j])
    cloud = tmp_cloud
    


# 답 만들기 모든 것의 합
answer =0
for i in range(n):
    answer += sum(data[i])


print(answer)