
def main():
   
    s = [int(input()) for i in range(1,10)]
    print(max(s))
    print(s.index(max(s))+1)
        
if __name__ == "__main__":
    main()

