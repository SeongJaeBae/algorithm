import sys
def main():
  n = int(input())
  s = list(map(int,input().split()))
  answer = []
  for i in s:
    c=0
    for j in range(1,i):
      if i%j ==0:
        c+=1
    if c==1:
      answer.append(i)
  print(len(answer))
main()