characters = input().rstrip()
password = input().rstrip()
char_val = {c: i for i,c in enumerate(characters, 1)}
N = len(characters)
power = 1
answer = 0
for i, p in enumerate(reversed(password)):
    answer = (answer + power * char_val[p]) % 900528
    power = (power * N) % 900528

print(answer)