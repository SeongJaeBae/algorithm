import sys
import math
input = sys.stdin.readline
answer = math.inf
r,c,k = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(3)]

def operation(arr, l) :
    for idx, row in enumerate(arr) :
        temp = []
        for n in set(row) : # 행의 중복을 제거한 후
            if n : # 0이 아닌 숫자면
                temp.append((n, row.count(n))) # 해당 숫자에 대한 값을 세어줌
        temp = sorted(temp, key = lambda x : (x[1], x[0])) # 개수, 숫자 순서로 정렬
        templen = len(temp)
        if templen > 50 : templen = 50 # 숫자의 개수는 100을 넘어가면 안됨
        l = max(l, templen * 2) # 행의 길이를 최대로 바꿔줌
        arr[idx] = [] # A의 idx행 초기화
        for i in range(templen) : # A의 idx행 재구성
            arr[idx].append(temp[i][0])
            arr[idx].append(temp[i][1])
    
    # 최대 길이만큼 0 채우기
    for idx, row in enumerate(arr) :
        for _ in range(l-len(row)) :
            arr[idx].append(0)
    
    return arr, l





rlen, clen = 3, 3

for time in range(101) :

    if r <= rlen and c <= clen and arr[r-1][c-1] == k :
        print(time)
        break
    if rlen >= clen : # R연산
        arr, clen = operation(arr, clen)
    else : # C연산
        arr, rlen = operation(list(zip(*arr)), rlen) # 행과 열을 전치시켜 함수를 실행한다.
        arr = list(zip(*arr)) # 행과 열을 원상태로 바꾼다.
else : # 100초 동안 r행 c열이 k가 아닌 경우
    print(-1)