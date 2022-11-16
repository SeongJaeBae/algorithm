from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)

"""
import copy
def make_next_step(size,m):
    state =0 # 0 -> -1 출력 해야하는 상태 / 1 -> 이번에 성공적으로 다음 스템으로 진행함

    #상하좌우
    t_x = [0,0,-1,1]
    t_y = [1,-1,0,0]
    
    next_map = copy.deepcopy(m)
    for i in range(size[1]):
        for j in range(size[0]):
            
            if m[i][j] == 1:
                for z in range(4):
                    if i+t_y[z] <0 or i+t_y[z] >= size[1]:
                        continue
                    elif j+t_x[z] <0 or j+t_x[z] >= size[0]:
                        continue

                    if next_map[i+t_y[z]][j+t_x[z]]== -1:
                        continue
                    elif next_map[i+t_y[z]][j+t_x[z]]== 0:
                        next_map[i+t_y[z]][j+t_x[z]] = 1
                        state=1

    if state == 0:
        return -1
    else:
        return next_map

def check_state(size, m):
    #1-> 끝 0->계속해서 진행 
    #-1 이면 더 진행 못하고 끝 -> step 에서 확인해서 리턴해야 할 듯
    end=1
    for i in range(size[1]):
        if 0 in m[i]:
            end =0
    
    return end
def main():
    size = list(map(int,input().split()))

    m = [list(map(int,input().split())) for i in range(size[1])]
    #1 = 익은 토마토 0 = 익지 않은 토마토 -1 토마토가 들어있지 않은칸
    #익은 토마토 기준 상하좌우가 익는다.
    
    #다 익지 못하는 경우 return -1
    #익힐 수 있는 경우 return i 몇 턴 뒤에 다 익는지
    #처음부터 끝나는 경우인 경우 return 0
    count =0
    #check_state
    while(check_state(size,m) ==0):
        tmp = make_next_step(size,m)
        if tmp == -1:
            return print("-1")  
        else:
            m = tmp
            count +=1
    return print(count)

if __name__ == "__main__":
    main()

"""