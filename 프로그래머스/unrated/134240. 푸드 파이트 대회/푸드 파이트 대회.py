def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if int(food[i]) >=2:
            for j in range(0,int(food[i]/2)):
                answer+=str(i)
    re = reversed(answer)
    answer +="0"
    answer += "".join(re)
    return answer