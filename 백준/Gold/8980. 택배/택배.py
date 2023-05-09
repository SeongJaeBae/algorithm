import sys
input = sys.stdin.readline
n,c =map(int,input().split())#2<=n 2000, 1<= c <= 10000
m = int(input())#1<= m <= 10000
boxes = [list(map(int,input().split())) for _ in range(m)]
#마을 번호, 박스를 받는 마을번호, 박스개수
boxes.sort(key=lambda x :  x[1])

# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.

#고려해야 되는 경우 1.. 용량에 제한되어서 싣지 못하는 경우 -> 일부만 들고감


count = 0
remains = [c]*(n+1) # 마을 당 수용가능한 박스 수

for i in range(m):
    temp = c # c개를 옮길 수 있다고 가정
    for j in range(boxes[i][0], boxes[i][1]):
        temp = min(temp, remains[j])
    temp = min(temp, boxes[i][2])
    for k in range(boxes[i][0], boxes[i][1]):
        remains[k] -= temp
    count += temp

print(count)