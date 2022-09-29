def solution(survey, choices):
    answer = ''
    # [R,T] [C,F] [J,M] [A,N]
    val_1,val_2,val_3,val_4 = 0,0,0,0
    for s,c in zip(survey,choices):
        if s == "RT":
            val_1 += c-4
        elif s == "CF":
            val_2 += c-4
        elif s == "JM":
            val_3 += c-4
        elif s == "AN":
            val_4 += c-4
        elif s == "TR":
            val_1 += 4-c
        elif s == "FC":
            val_2 += 4-c
        elif s == "MJ":
            val_3 += 4-c
        elif s == "NA":
            val_4 += 4-c
            
    #-3 -2 -1 0 1 2 3
    
    if val_1 <= 0:
        answer += "R"
    else:
        answer += "T"
        
    if val_2 <= 0:
        answer += "C"
    else:
        answer += "F"
        
    if val_3 <= 0:
        answer += "J"
    else:
        answer += "M"
        
    if val_4 <= 0:
        answer += "A"
    else:
        answer += "N"

    
    return answer