import sys
sys.setrecursionlimit(1000001)
vis = [False] * 1000001

def solution(n, lighthouse):
    graph = [[] for i in range(n+1)]
    for a,b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(u):
        vis[u] = True
        # if len(graph[u]) ==1:
        #     return 1, 0 # on, off
        # u가 leaf가 아니라면
        on, off = 1, 0
        for v in [v for v in graph[u] if not vis[v]]:
            child_on, child_off = dfs(v)
            on += min(child_on, child_off)
            off += child_on
        return on, off
    on, off = dfs(1)        
    return min(on, off)