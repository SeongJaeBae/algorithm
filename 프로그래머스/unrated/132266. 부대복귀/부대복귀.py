from collections import deque
import math
def solution(n, roads, sources, destination):
    answer = []
    link = [[] for i in range(n+1)]
    
    for i in roads:
        link[i[0]].append(i[1])
        link[i[1]].append(i[0])
        
    q = deque()
    q.append(destination)
    
    v = [-1 for i in range(n+1)]
    v[destination] = 0
    
    while q:
        now = q.popleft()
        for i in link[now]:
            if v[i] == -1:
                v[i] = v[now] +1
                q.append(i)
                
    answer = [v[i] for i in sources]
    return answer