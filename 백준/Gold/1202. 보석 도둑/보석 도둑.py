import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
n,k = map(int, input().split())
zem = [list(map(int, input().split())) for _ in range(n)]
c = [int(input()) for _ in range(k)]
c.sort()
zem.sort()

answer = 0
tmp=[]
#0 = 무게, 1 -> 가격
#무게는 c 의 i 번째 값을 넘지 않으면서 만족하는 가치의 최대를 구해야함
for i in c:# k 번 돌아감 -> k > n 인경우가 존재함
    while zem and i >= zem[0][0]:
      heapq.heappush(tmp, -zem[0][1])
      heapq.heappop(zem)
    if tmp:
        answer -= heapq.heappop(tmp)
print(answer)