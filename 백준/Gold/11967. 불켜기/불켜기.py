from sys import stdin
input = stdin.readline
from collections import deque, defaultdict

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    result = 1      # 불 켤 수 있는 방의 갯수
    visited = [[0] * N for _ in range(N)]   # 방문 표시
    visited[0][0] = 1
    lights = [[0] * N for _ in range(N)]    # 불 켠 방 표시
    lights[0][0] = 1
    Q = deque([(0, 0)])
    while Q:
        r, c = Q.popleft()
        for tr, tc in turnInfo[(r, c)]:   # 불 켤 수 있는 곳(딕셔너리 참조)
            if not lights[tr][tc]:
                lights[tr][tc] = 1      # 새로 불 켜기
                result += 1
                for d in range(4):      # 4방향 연결된 곳
                    nr = tr + dr[d]
                    nc = tc + dc[d]
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if visited[nr][nc]:     # 방문한 적 있으면(새로 연결되어 또 불을 켤 곳이 있을 수 있으므로)
                        Q.append((nr, nc))  # 큐에 담기
        
        # 현 위치를 기준으로
        for d in range(4):      # 4방향 연결된 곳
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 첫 방문인데 이미 불 켜진 곳이면
            if not visited[nr][nc] and lights[nr][nc]:
                Q.append((nr, nc))      # 재검사를 위해 큐에 담기
                visited[nr][nc] = 1     # 방문 표시
                
    return result


# main
N, M = map(int, input().split())
turnInfo = defaultdict(list)	# 각 위치에서 불 켤 수 있는 위치 정보 저장
for _ in range(M):
    sr, sc, tr, tc = map(int, input().split())
    turnInfo[(sr-1, sc-1)].append((tr-1, tc-1))

print(bfs())