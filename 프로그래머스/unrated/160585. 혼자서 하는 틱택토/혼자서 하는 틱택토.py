def solution(board):
    cnt1 = sum([a.count("O") for a in board])
    cnt2 = sum([a.count("X") for a in board])
    tmp = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], 
           [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
           [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
    a = sum([all([board[x][y] == "O" for x, y in arr]) for arr in tmp])
    b = sum([all([board[x][y] == "X" for x, y in arr]) for arr in tmp])
    if not (0 <= cnt1 - cnt2 <= 1): return 0
    if a + b > 1 and not (a == 2 and b == 0 and cnt1 - cnt2 == 1): return 0
    if a == 1 and cnt1 == cnt2: return 0
    if b == 1 and cnt1 > cnt2: return 0
    return 1