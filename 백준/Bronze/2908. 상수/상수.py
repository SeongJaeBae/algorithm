
def main():
    s = input().split()
    a = s[0]
    b = s[1]
    a = a[::-1]
    b = b[::-1]
    print(max(int(a),int(b)))
        
if __name__ == "__main__":
    main()

