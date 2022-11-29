import sys
def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = list(set(s))
    s.sort()
    s.sort(key=len)
    for i in s:
        print(i)
      
main()