
def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in s:
        answer =0
        before =0
        for j in range(len(i)):
            if i[j] =="O":
                before += 1
                answer += before
            else:
                before =0
        print(answer)
        
if __name__ == "__main__":
    main()

