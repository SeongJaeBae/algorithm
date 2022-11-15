
def main():
    n = int(input())
    s = input()
    answer = 0
    for i in range(n):
        answer += int(s[i])
    print(answer)
if __name__ == "__main__":
    main()

