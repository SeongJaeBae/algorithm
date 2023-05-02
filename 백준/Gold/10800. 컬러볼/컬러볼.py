import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(100000)
answer = []
ball = []
n = int(input())#1~200000
for i in range(n):
        c, s = map(int, sys.stdin.readline().split())
        ball.append([c, s, i])

#i 번째 플레이어보다 크기가 작고 색이 다른공 먹으면 그 크기만큼 점수 어등ㅁ
#잡아 먹어도 변화는 없음
ball.sort(key=lambda x: x[1])

answer = defaultdict(int)
ball_size_sum = defaultdict(int)  # 색깔 별 공의 크기 누적합
total = 0  # 총합
i, j = 0, 0
for i in range(n):
    while ball[j][1] < ball[i][1]:  # 크기가 작을 때까지 수행
        total += ball[j][1]
        ball_size_sum[ball[j][0]] += ball[j][1]
        j += 1
    answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]  # 총합 - 현재 색깔 공 누적합
for i in range(n):
    print(answer[i])
