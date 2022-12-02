def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            answer +=1
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
        
        
    return answer