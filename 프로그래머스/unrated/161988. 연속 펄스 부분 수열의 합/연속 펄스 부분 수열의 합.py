def solution(sequence):
    answer = 0
    #음수 양수 번갈아나오는 수열을 부분수열에 곱해서 나오는 최대값 구하기
    n = len(sequence)
    p_dp = [0] * n
    p_dp[0] = sequence[0]
    m_dp = [0] * n
    m_dp[0] = sequence[0]
    plus = [1 if i %2 == 0 else -1 for i in range(n)]
    minus = [-1 if i %2 == 0 else 1 for i in range(n)]
    
    if n ==1:
        return abs(sequence[0])
    
    for i in range(n):
        p_dp[i] = max(p_dp[i-1]+sequence[i]*plus[i],sequence[i]*plus[i])
        m_dp[i] = max(m_dp[i-1]+sequence[i]*minus[i],sequence[i]*minus[i])
        
    max_p = max(p_dp)
    max_m = max(m_dp)
        
    return max(max_p,max_m)