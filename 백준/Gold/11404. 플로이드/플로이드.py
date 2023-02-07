import sys

n = int(input())
m = int(input())
graph = [[999999999 for i in range(n)] for j in range(n)]

for i in range(m):
    line = list(map(int,input().split()))
    if graph[line[0]-1][line[1]-1] == -1 or graph[line[0]-1][line[1]-1] > line[2] :
        graph[line[0]-1][line[1]-1] = line[2]
answer = [[]* n]
for t in range(n):
    for i in range(n):
        for j in range(n):
            if i== j :
                graph[i][j] =0
            else :
                graph[i][j] = min(graph[i][j], graph[i][t]+graph[t][j])
    
for i in graph[:]:
    for j in i:
        if j == 999999999:
            print("0",end=" ")
        else:
            print(j,end=" ")
    print()
