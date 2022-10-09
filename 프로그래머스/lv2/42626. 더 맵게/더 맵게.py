from heapq import *

def solution(scoville, K):
    count = 0
    heapify(scoville)
    n = len(scoville)
    while scoville[0] < K and n > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
        n -= 1
    return count if scoville[0] >= K else -1