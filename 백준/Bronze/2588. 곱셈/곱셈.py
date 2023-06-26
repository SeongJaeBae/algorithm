from sys import stdin
input = stdin.readline

answer = 0
a = int(input())
b = int(input())
tmp = str(b)
print(a * int(tmp[2]))
print(a * int(tmp[1]))
print(a * int(tmp[0]))
print(a * b)