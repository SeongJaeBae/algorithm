import sys
sys.setrecursionlimit(100000)
check = False
def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''

    directions = ['d', 'l', 'r', 'u']
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    def dfs(px, py, cnt, way):
        
        global check, answer
        if check:
            return
        
        if cnt > k:
            return
        
        if abs(px - r) + abs(py - c) + cnt > k:
            return
            
        if not check and cnt == k:
            if px == r and py == c:
                check = True
                answer = way
            return

        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue

            dfs(nx, ny, cnt + 1, way + directions[d])

    z = k - abs(x - r) + abs(y - c)
    if z < 0 or z % 2 != 0:
        return 'impossible'
    
    dfs(x, y, 0, '')
    if not check:
        return "impossible"

    return answer