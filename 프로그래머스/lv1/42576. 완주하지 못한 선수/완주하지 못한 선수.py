import collections
def solution(participant, completion):
    answer = ''
    p = sorted(participant)
    c = sorted(completion)
    
    answer = collections.Counter(participant)- collections.Counter(completion)
    
    return list(answer)[0]
