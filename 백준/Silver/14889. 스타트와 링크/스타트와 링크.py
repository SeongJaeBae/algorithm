import itertools
def main():
    n = int(input())
    arr = []
    [arr.append(list(map(int,input().split(" "))) ) for i in range(0,n)]
    
    case = itertools.combinations(range(n),int(n/2))
    min = 100
    for c in case:
        tmp1 =0
        tmp2 =0
        tmp_min = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif j in c and i in c:
                    tmp1 += arr[i][j]
                elif j not in c and i not in c:
                    tmp2 += arr[i][j]
        if tmp1 > tmp2:
            tmp_min = tmp1- tmp2
        else:
            tmp_min = tmp2 - tmp1
        
        if tmp_min == 0:
            print(0)
            return 0
        if min > tmp_min:
            min = tmp_min
    print(min)
    return min

    
   

if __name__ == "__main__":
    main()


