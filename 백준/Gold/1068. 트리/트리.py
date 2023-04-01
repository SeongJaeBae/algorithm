from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
target = int(input())

#트리 구조 만들기
tree = defaultdict(list)
for i in range(0,n):
    if i == target :
        continue
    tree[s[i]].append(i)

#리프 노드 개수 세기
def count_leaf(idx):
    if tree[idx] == []:
        return 1
    tmp_sum = 0
    for i in tree[idx]:
        tmp_sum += count_leaf(i)
    return tmp_sum

#루트 안주는 경우 시부럴
if tree[-1] == []:
    print(0)
else:
    print(count_leaf(-1))

