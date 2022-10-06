from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for i in permutations(dungeons, n):  
        now_k = k
        tmp_max =0
        for j in i:
            if now_k >= j[0]:
                tmp_max +=1
                now_k -= j[1]
            else:
                break
        answer = max(answer,tmp_max)

    return answer