import sys
def main():
  answer =[]  
  while 1:
    s = list(map(int,sys.stdin.readline().split()))
    s.sort()
    if sum(s) ==0:
      return print("\n".join(answer))
    else:
      #피타고라스
      if pow(s[2],2) == pow(s[0],2) + pow(s[1],2):
        answer.append("right")
      else:
        answer.append("wrong")

    
main()