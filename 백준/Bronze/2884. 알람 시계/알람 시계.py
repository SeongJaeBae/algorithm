
def main():
    s =  list(map(int,input().split()))
    
    if s[1] >= 45:
        print(s[0], s[1]-45)
    elif s[0] == 0:
        print("23", s[1]+15)
    else:
        print(s[0]-1, s[1]+15)    
  
        
if __name__ == "__main__":
    main()

