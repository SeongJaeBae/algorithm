
def main():
    s = list(map(int,input().split()))
    if s == sorted(s):
        print("ascending")
    elif s == sorted(s,reverse=True):
        print("descending")
    else:
        print("mixed")
        
if __name__ == "__main__":
    main()

