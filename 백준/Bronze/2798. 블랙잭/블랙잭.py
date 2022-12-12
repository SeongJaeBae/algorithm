import itertools
import sys
def main():
    answer = 0
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    for i in itertools.permutations(b,3):
        tmp = sum(i)
        if sum(i) > a[1]:
            continue
        else:
            answer = max(tmp,answer)
    return print(answer)

main()