import sys
input = sys.stdin.readline
N, K = map(int,input().split())

data = []
for _ in range(K):
    X, R, C = map(int,input().split())
    data.append([X, (X-1)//N , (X-1) % N  , R-1, C-1]) # X//N 주의.. 인덱스값으로 생각하고 값을 설정했기 때문에 현재 좌표와 목표좌표 모두 -1


def move_target(n, t, N):                               # 타겟을 목표 지점으로 옮기는 함수
    moved = 0 
    if n < t:                                           # 현재위치 n이 타켓 t보다 앞쪽에 위치하면 이동값은 t-n
        moved += t-n
    elif n > t:                                         # 현재 위치가 타켓 뒤라면 한바퀴 돌아서 이동해야하기때문에 N - n + t
        moved += N - n
        moved += t
    return moved

def turn_the_table(d):                                  # 표를 회전하는 함수 
    global turn, N

    x, rn, cn, rt, ct = data[d]                         # data에 담았던 수를 언패킹 rn cn (row now, colum now) / rt ct (row target, colum target)

    mr = move_target(rn, rt, N)                         # 열과 행을 각각 이동시키고 mr mc (move row, move colum) 변수에 이동한 거리를 담아준다
    mc = move_target(cn, ct, N)
    turn = turn + mc + mr                               # 움직인 횟수만큼 turn 변수에 반영

    for d2 in range(d+1, K):                            # data에서 현재 인덱스인 d 이후의 데이터를 순회한다 
        if data[d2][0] == x:                            # 현재 trun_the_table에서 이동한 숫자 x와 데이터의 숫자가 같다면 지금 이동한 좌표(target row,col)로 이동
            data[d2][1] = rt
            data[d2][2] = ct
        else:
            if data[d2][1] == rn:                       # 같은 row에 위치한다면 
                data[d2][2] += mc                       # 이동한 col 만큼 좌표값 변경
                if data[d2][2] >= N:
                    data[d2][2] = data[d2][2] % N
            if data[d2][2] == ct:                       # 같은 col에 위치한다면
                data[d2][1] += mr                       # 이동한 row 만큼 좌표값 변경
                if data[d2][1] >= N:
                    data[d2][1] = data[d2][1] % N

for d in range(K):                                      # 총 데이터 개수인 K만큼 반복
    turn = 0                                            # 매 데이터마다 turn(회전수) 구해서 출력
    turn_the_table(d)
    print(turn)