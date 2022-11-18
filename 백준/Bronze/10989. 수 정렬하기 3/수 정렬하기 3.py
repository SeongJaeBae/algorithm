import sys
def main():
    n = int(input())
    answer = [0] * 10001
    for i in range(n):
        answer[int(sys.stdin.readline())] +=1

    #n ~ 천만이다. 메모리 터진다.
    for i in range(10001):
        if answer[i] != 0:
            for j in range(answer[i]):
                print(i)
if __name__ == "__main__":
    main()

