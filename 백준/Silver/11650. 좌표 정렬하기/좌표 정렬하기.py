import sys
def main():
    n = int(input())
    s = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
    s.sort()

    for i in s:
        print(int(i[0]), int(i[1]))

main()