
def main():
    n = int(input())

    for i in range(n-1,-1,-1):
        tmp = ""
        for j in range(i):
            tmp += " "
        for j in range(n-i):
            tmp += "*"
        print(tmp)
        
if __name__ == "__main__":
    main()

