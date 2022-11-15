
def main():
    t = int(input())
    arr = [input().split() for i in range(t)]
    for i in arr:
        tmp = ""
        for j in range(len(i[1])):
            for z in range(int(i[0])):
                tmp += i[1][j]
        print(tmp)
        
if __name__ == "__main__":
    main()

