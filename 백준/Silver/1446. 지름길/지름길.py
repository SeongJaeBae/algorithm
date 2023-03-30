
n, d = map(int,input().split())

short = [list(map(int,input().split())) for i in range(n)]
answer = [i for i in range(10001)]
#시작 위치 ~ 종료 위치 사이에 있는 지름길만 이용 가능
short = sorted(short, key = lambda x : x[1])

for start,end,value in short:
    if answer[end] > answer[start] + value:
        answer[end] = answer[start] + value
        answer[end :] = range(answer[start] + value, 10001- (answer[start] + value))

print(answer[d])