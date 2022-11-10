def solution(ingredient):
    answer = 0
    #오호 이거 DP네~ 이전 문제랑 똑깥네??
    #1231 -> pop
    #1을 서치 -> 1. i 가 3보다 크고 [-3:] 까지의 stack이 1231 일 때 -> pop
    dp = []
    if len(ingredient)<4:
        return 0
    dp = []
    dp.append(ingredient[0])
    dp.append(ingredient[1])
    dp.append(ingredient[2])
    for i in range(3,len(ingredient)):
        dp.append(ingredient[i])
        if ingredient[i]==1 and dp[-4:] == [1,2,3,1]:#
            answer+=1
            dp.pop()
            dp.pop()
            dp.pop()
            dp.pop()
    
    return answer