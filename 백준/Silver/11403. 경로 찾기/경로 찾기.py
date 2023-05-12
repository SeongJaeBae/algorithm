from sys import stdin
from collections import deque

def bfs(graph, x):
    visited = [0] * N
    queue = deque([x])
    while queue:
        current = queue.popleft()
        for i in range(N):
            if not visited[i] and graph[current][i]:
                queue.append(i)
                visited[i] = 1
    return visited

N = int(stdin.readline())
graph = [list(map(int, line.split())) for line in stdin.readlines()]
answer = []
for i in range(N):
    print(*bfs(graph, i))