import sys
input = sys.stdin.readline

N,e,w,s,n = map(int,input().split())

# 동,서,남,북
dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 동,서,남,북 에맞춰서 값들을 넣어준다,.
percent_data= [e,w,s,n]

#주어진 N을 기점으로 N,N이 한가운데 오는 2차원 배열을 만들어준다.
graph = [[0] * (2*N+1) for _ in range(2*N+1)]

answer = 0
def dfs(x,y,percent,cnt):
    # 전역변수로 만들어서 모든 dfs함수가 실행될 떄 cnt == N 이면  answer에 확률들을 더하게 한다.
    global answer
    if cnt == N:
        # 여기서 주의할 점은 확률을 곱하는게 아니라 더해주는 점.
        answer += percent
        return
    # 현재 좌표의 확률을 now_percent에 담아둔다.
    now_percent = percent
    # 방문처리
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < (2*N+1) and 0<=ny < (2*N+1):
            # 이미 방문했으면 continue
            if graph[nx][ny] == 1:
                continue
            # 방문 안했으면, 이동할 좌표, 이동하는곳의 확률을 현재 확률에 곱해주고, cnt +1 해준다.
            else:
                # 동서남북 순서에 따라서 percent_data를 맞춰준다. 곱할 때는 100으로 나워서 계산
                dfs(nx,ny,now_percent*(percent_data[i]/100),cnt+1)
                # dfs함수 실행시켜주고, 다른 Dfs 함수들의 실행을 위해 방문처리를 해제 해준다.
                graph[nx][ny] = 0

dfs(N,N,1,0)

print(answer)