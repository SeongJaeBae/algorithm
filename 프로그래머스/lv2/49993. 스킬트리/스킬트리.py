import itertools as iter
def solution(s, st):
    answer = 0
    
    s_n = len(s)
    s_list = list(s)
    tmp = []
    for i in st:
        tmp.clear()
        tmp_n = 0
        for j in i :
            if j in s_list:
                tmp.append(s_list.index(j))
                tmp_n +=1
        if (tmp == sorted(range(0,tmp_n))):
            answer +=1
        
        
    return answer