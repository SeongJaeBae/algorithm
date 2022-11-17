
    

def main():
    s = list(map(int,input().split()))
    x = abs(s[2]-s[0])
    y = abs(s[3]-s[1])
    x = min(x,s[0])
    y = min(y,s[1])
    print(min(x,y))

if __name__ == "__main__":
    main()

