from collections import Counter
def solution(X, Y):
    arr = []
    
    countx = Counter([int(i) for i in X])
    county = Counter([int(i) for i in Y])
    
    inter = countx & county
    for key,value in inter.items():
        temp = [key] * value
        arr.extend(temp)
    
    result = ''.join(map(str,sorted(arr, reverse=True)))
    
    if result == '':
        return "-1"
    
    if list(set(result)) == ['0']:
        return "0"  
    
    return result