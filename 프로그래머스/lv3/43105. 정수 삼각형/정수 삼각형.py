
def solution(tri):
    answer = 0
    h = len(tri)
    tmp = [[0 for j in range(len(tri[i]))] for i in range(h)]
    #연산해서 각각의 위치에서의 최대값 할당하는 방식으로 
    if h ==1:
        return tri[0][0]
    
    tmp [0][0] = tri[0][0]
    for i in range(h):
        for j in range(len(tri[i])):
            if i == 0:
                continue
            if j == 0:
                tmp[i][j] = tri[i][j] + tmp[i-1][j]
                continue
            if j == i:
                tmp[i][j] = tri[i][j] + tmp[i-1][j-1]
                continue
            tmp[i][j] = max(tri[i][j] + tmp[i-1][j-1], tri[i][j] + tmp[i-1][j])
    return max(tmp[h-1])