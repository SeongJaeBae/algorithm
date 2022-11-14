from collections import Counter
def solution(s):
    answer = []
    i = 0
    j = 0
    while s != "1":
        i +=1
        c = Counter(s)
        j += c["0"]
        s = s.replace("0","")
        s = bin(len(s))[2:]
      
    return [i,j]