import sys
#큐를 사용하기 위해 임포트
from collections import deque

n = int(sys.stdin.readline())
queue =deque([i for i in range(1,n+1) ])
t =1

for i in range(n-1):
    number = (t**3) % len(queue)
    if number == 1:
        queue.popleft()
    #첫번째 사람이 탈락하는게 아니라면
    #number-1번째 사람이 탈락한다.
    #왼쪽(시작하는 쪽)에서 number-1번째 사람이 탈락해야하므로
    #매개변수를 음수로 넣어준다.
    else:    
        queue.rotate(-(number-1))            
        queue.popleft()
    t+=1
print(queue.pop())
