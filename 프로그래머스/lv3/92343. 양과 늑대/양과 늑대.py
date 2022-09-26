def dfs(idx, sheep, wolf, node):
    global g_info, answer, graph
    
    if g_info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1
    if wolf >= sheep:
        return
    
    node.extend(graph[idx])
    print(idx, sheep, node)
    for i in node:
        dfs(i,sheep,wolf, [j for j in node if i != j])
def solution(info, edges):
    global answer, g_info, graph
    answer = 0
    #늑대 >= 양 -> 양 다 잡아먹음
    #잡아먹히지 않는 최대한의 양의 수
    #info 0-> sheep 1-> wolf info 0 is always 0
    # 이진 트리 만들기
    g_info = info
    n= len(info)
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
    print(graph)
    
    # dfs 돌리기
    dfs(0, 0, 0, [])
    return answer