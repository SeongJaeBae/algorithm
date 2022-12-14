
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
from collections import deque
def solution(q1, q2):
    cnt = 0
    q1 = deque(q1)
    q2 = deque(q2)
    all = q1+q2

    #합이 홀수면 -1
    if sum(all)%2 == 1:
        return -1
    #합이 짝수이면서 안되는 경우(1개의 항이 합의 절반을 넘길 경우)
    if max(all) > (sum(all)/2) :
        return -1

    #합이 짝수이면서 되는 경우 -> r l 두개의 경우의 수로 돌리면 될 듯
    #dfs 하면 무한루프 걸릴수도?-> 걸림
    #bfs로 while 돌리자
    s1 = sum(q1)
    s2 = sum(q2)
    limit = 3*len(q1)
    while s1 != s2:
        if s1 > s2:
            tmp = q1.popleft()
            q2.append(tmp)
            s1 -= tmp
            s2 += tmp
            cnt += 1
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            s1 +=tmp
            s2 -=tmp
            cnt +=1
        if cnt > limit:
            return -1


    return cnt