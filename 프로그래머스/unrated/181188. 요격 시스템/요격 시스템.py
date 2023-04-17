def solution(targets):
    answer = 0
    # n 500000 까지, se 0 ~ 0~1억까지
    tmp_max = len(targets)
    targets.sort()
    tmp_s,tmp_e = 0,0
    for i in range(len(targets)):
        if i == 0:
            tmp_s = targets[i][0]
            tmp_e = targets[i][1]
            answer +=1
            continue
        if tmp_s <= targets[i][0] and tmp_e >targets[i][0]:
            tmp_s = max(tmp_s,targets[i][0])
            tmp_e = min(tmp_e,targets[i][1])
        else:
            tmp_s = targets[i][0]
            tmp_e = targets[i][1]
            answer+=1
        
        
        
    return answer