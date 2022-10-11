def solution(babbling):
    answer = 0
    can = ["aya","ye","woo","ma"]
    for i in babbling:
        for j in can:
            if j*2 in i:
                break
            if j in i:
                i = i.replace(j,"")
                
        if len(i) ==0:
            answer+=1
    return answer