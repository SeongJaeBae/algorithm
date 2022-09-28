def solution(n):
    
    for i in range(1,n):
        if n % i == 1:
            print(i)
            return i
    return n-1