import sys
input = sys.stdin.readline
answer = 0 
n = int(input())
def rec(arr,n):
    length = len(arr)
    for i in range(1,length//2 +1):
        if arr[-i:] == arr[-(2 *i): -i]:
            return -1
    
    if len(arr)==n:
        print(arr)
        return 0
    for i in range(1,4):
        #아니면 스탑
        if rec(arr+str(i),n) == 0:
            return 0
        

rec("1",n)

