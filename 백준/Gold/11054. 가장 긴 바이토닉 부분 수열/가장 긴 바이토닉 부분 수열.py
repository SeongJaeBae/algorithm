n = int(input())
s = list(map(int,input().split()))
reverse = s[::-1]

plus = [1 for i in range(n)]
minus = [1 for i in range(n)]
#가장 긴 증가하는 수열
#가장 긴 감소하는 수열 
#가장 긴 바이토닉 수열 -> 가장 긴 증가 수열 + 감소수열?
for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            plus[i] = max(plus[i],plus[j]+1)
        if reverse[i]> reverse[j]:
            minus[i] = max(minus[i],minus[j]+1)
#print(plus)
#print(minus)
answer = [0 for i in range(n)]
for i in range(n):
    answer[i] = plus[i] + minus[n-i-1] -1

print(max(answer))