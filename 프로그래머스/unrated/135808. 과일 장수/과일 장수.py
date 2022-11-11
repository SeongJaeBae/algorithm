def solution(k, m, score):
    answer = 0
    score = sorted(score)
   
    k = int(len(score)/m)
    for i in range(k):
        answer += min(score[-m:]) * m
        for j in range(m):
            score.pop()
    return answer