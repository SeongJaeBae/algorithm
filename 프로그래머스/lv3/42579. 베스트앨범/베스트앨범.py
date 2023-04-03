def solution(genres, plays):
    answer = []
    data = [[i,genres[i], plays[i],0] for i in range(len(genres))]
    data = sorted(data,key=lambda x :x[1])
    #data = sorted(data)
    #장르 합 계산
    ex_genres = data[0][1]
    tmp_sum = 0
    tmp_idx = 0
    for i in range(len(genres)):
        if data[i][1] == ex_genres:
            tmp_sum += data[i][2]
        else:
            #이전꺼 업데이트
            for j in range(tmp_idx,i):
                data[j][3] = tmp_sum
            #바뀐거로 업데이트
            tmp_idx = i
            ex_genres = data[i][1]
            tmp_sum = data[i][2]
    for j in range(tmp_idx,len(genres)):
        data[j][3] = tmp_sum
        
    data = sorted(data,key=lambda x :(-x[3],-x[2],x[0]))
    print(data)
    ex_genres = data[0][1]
    stack = []
    counter =0
    
    for i in range(len(genres)):
        if data[i][1] == ex_genres:
            counter +=1
            if counter <= 2:
                answer.append((data[i][0]))
        else:
            counter =1
            answer.append(data[i][0])
            ex_genres = data[i][1]
    
    
    return answer