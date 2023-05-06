from sys import stdin

def solution(preord, inord):
    def post_order(parent, left, right):
        val = ""
        if left > right:
            return val
        p_idx = inord.index(preord[parent])
        val += post_order(parent + 1, left, p_idx - 1)
        val += post_order(parent + p_idx - left + 1, p_idx + 1, right)
        return val + preord[parent]
    return post_order(0, 0, len(preord) - 1)

# pre-order : 부모 -> 왼쪽 -> 오른쪽
# in-order : 왼쪽 -> 부모 -> 오른쪽
# post-order : 왼쪽 -> 오른쪽 -> 부모
cases = stdin.readlines()
for c in cases:
    p, i = c.split()
    print(solution(p, i))