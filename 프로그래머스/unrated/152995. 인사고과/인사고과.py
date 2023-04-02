def solution(scores):
    oh = scores[0]
    oh_sum = sum(oh)
    answer = 1
    scores.sort(key=lambda x:(-x[0], x[1]))
    tmp = 0
    for score in scores:
        if oh[0] < score[0] and oh[1] < score[1]:
            return -1
        
        if oh_sum < sum(score) and tmp <= score[1]:
            answer += 1
            tmp = score[1]
    

    return answer