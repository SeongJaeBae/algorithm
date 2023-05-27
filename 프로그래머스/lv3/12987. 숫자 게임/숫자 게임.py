def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    a_idx = 0
    b_idx = 0
    while  1:
        if a_idx == len(A) or b_idx == len(B):
            break
        if B[b_idx] > A[a_idx]:
            answer +=1
            b_idx +=1
            a_idx +=1
        else:
            a_idx+=1
            
            
    return answer