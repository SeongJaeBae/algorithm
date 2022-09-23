def solution(str1, str2):
    answer = 0
    
    #2 단어씩 끝어서 세트 만들기-> 중복 허용
    #2-1 끝은 단어에서 특수문자 항 버리기/ 대소문자 전처리
    l1, l2 = [],[]
    for i in range(len(str1)-1):
        tmp = str1[i]+str1[i+1]
        if tmp.isalpha():
            l1.append(tmp.lower())
        
    for i in range(len(str2)-1):
        tmp = str2[i]+str2[i+1]
        if tmp.isalpha():
            l2.append(tmp.lower())
    
    #3 s1 s2 교집합 / 합집합 
    tmp = l2.copy()
    l_and = []
    for i in l1:
        if i in tmp:
            l_and.append(i)
            tmp.remove(i)
    
    l_or = l1.copy()
    tmp = l1.copy()
   
    for i in l2:
        if i not in tmp:
            l_or.append(i)
        else:
            tmp.remove(i)
    
    if len(l_and) != 0 or len(l_or) != 0:
        answer = len(l_and)/ len(l_or)
        answer= answer * 65536
    else:
        answer = 65536
    
    return int(answer)