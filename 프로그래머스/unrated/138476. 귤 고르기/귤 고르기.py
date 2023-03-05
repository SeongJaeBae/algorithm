from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    sum = 0
    for i,j in count.most_common():
        sum += j
        answer += 1
        if sum >= k:
            return answer
