import sys
input = sys.stdin.readline


def knigt_moves(l: int) -> int:
    cnt = 0
    s_i, s_j = map(int, input().split())
    e_i, e_j = map(int, input().split())
    if s_i == e_i and s_j == e_j:  return cnt

    visited = [[False] * l for _ in range(l)]
    visited[s_i][s_j] = True
    q = [(s_i, s_j)]

    while q:
        cnt += 1
        tmp = []
        for i, j in q:
            for ni, nj in zip(map(lambda ii: i+ii, di), map(lambda jj: j+jj, dj)):
                if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                    if ni == e_i and nj == e_j:
                        return cnt
                    tmp.append((ni, nj))
                    visited[ni][nj] = True
        q = tmp


if __name__ == '__main__':
    di = [-2, -2, -1, -1, 1, 1, 2, 2]
    dj = [-1, 1, -2, 2, -2, 2, -1, 1]
    print('\n'.join(str(knigt_moves(int(input()))) for _ in range(int(input()))))