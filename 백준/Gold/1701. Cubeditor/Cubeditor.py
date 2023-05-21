import sys
# failure : failure 배열을 리턴하는 함수
def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        # i가 가리키는 문자와 j가 가리키는 문자가 다르다면
        # j - 1의failure로 j는 이동해야 한다
        # 어쨌든 현재 i와 j가 다르지만 j - 1까지의 비교는 완료되었기 때문이다
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
            
        # i가 가리키는 문자와 j가 가리키는 문자가 같다면
        # j를 1증가시키고 failure[i]의 값을 1 증가시킨다
        # 왜냐면 j는 0부터 j까지 문자열 중 가장 길게 매칭된 부분 패턴의 길이를 의미하기 때문이다
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

# 입력부
pat = sys.stdin.readline().rstrip()

ans = 0
for i in range(len(pat)):
    # 잠재적인 패턴이 될 수 있는 모든 패턴에 대하여 failure 배열을 얻은 후 최대값을 갱신한다
    ans = max(ans, max(failure(pat[i:])))
    
# 정답 출력
print(ans)