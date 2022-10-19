from collections import deque
def recursive(p):
    if len(p) ==0:
        return ""
    answer = ""
    a=0
    b=0
    u = []
    v = []
    for i in range(0,len(p)):
        if p[i] == "(":
            a +=1
        else:
            b+=1
        if a==b:
            u = p[:i+1]
            v = p[i+1:]
            break
        
    if check_v(deque(u)):
        return u + recursive(v)
    else:#u 소팅하기
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer
       
def check_v(p):
    
    tmp_q = deque()
    u = deque()
    val_before= ""
    while p :
        if p:
            tmp = p.popleft()
        if len(tmp_q) ==0:
            tmp_q.append(tmp)
            continue
        if tmp_q[len(tmp)-1] =="(" and tmp == ")":
            i = tmp_q.pop()
            u.append(i)
            u.append(tmp)
            #print(tmp_q,u)
            #같으면 둘다 빼줌 
        else:
            tmp_q.append(tmp)
            #print(tmp_q,u)
    if len(tmp_q):
        return False
    return True # 올바른
def solution(p):
    answer = ''
    #u = 올바른 문자 괄호열,v = 균형 but 쌍 안맞음 
    tmp = deque(p)
    i = check_v(tmp)
    if i:
        return p
    else:
        answer = recursive(p)
        
    return answer