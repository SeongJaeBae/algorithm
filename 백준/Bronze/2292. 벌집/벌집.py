
def main():
    n= int(input())
    if n ==1:
        return print("1")
    #피보나치로 +6
    #1 7 19 37 61 // 1, 1+6, 1+6+12, 1+6+12+18 +6k
    t = 1
    for i in range(n):
        t += 6*(i+1)
        if t>= n:
            return print(i+2)
if __name__ == "__main__":
    main()