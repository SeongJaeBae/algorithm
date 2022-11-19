import sys
def main():
    n = int(input())
    answer = []
    for i in range(n):
        answer.append(int(sys.stdin.readline()))
    
    for i in sorted(answer):
        print(i)
if __name__ == "__main__":
    main()

