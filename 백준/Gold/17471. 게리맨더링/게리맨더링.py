
N = int(input())
p = list(map(int,input().split()))
cities = [ list(map(int,input().split()))[1:] for _ in range(N)]
T = [0 for _ in range(N)]
ans = 12341234132412345134123

#연결되어있는지 아닌지
def link(city,k):
    q = []
    for i in range(N):
        if city[i] == k:
            city[i] += 2
            q.append(i)
            break

    while q:
        t = q.pop() # 노드 번호
        # print(t)
        for c in cities[t]:
            if city[c-1] == k:
                city[c-1] += 2
                q.append(c-1)
    if k in city:
        return False
    return True
    
#부분집합 만드는 함수
def powerset(x):
    global ans
    a = 0
    b = 0
    if x ==  N:
        if sum(T) == N or sum(T) == 0:
            return

        temp_T = T[:]
        if link(temp_T,1) and link(temp_T,0): # 둘 다 연결되어 있을 경우에만
            for i in range(N):
                if T[i] == 1:
                    a += p[i]
                else:
                    b += p[i]
            temp_cnt = abs(a - b)

            if ans > temp_cnt:
                ans = temp_cnt
                return
    else:
        T[x] = 1
        powerset(x+1)
        T[x] = 0
        powerset(x+1)





powerset(0)
if ans == 12341234132412345134123:
    print(-1)
else:
    print(ans)