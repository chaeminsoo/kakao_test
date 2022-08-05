# 2022 KAKAO BLIND RECRUITMENT

def solution(board, skill):
    r = len(board)
    c = len(board[0])
    ref_board = [[0]*c for _ in range(r)]
    for t,r1,c1,r2,c2,dg in skill:
        if t == 1:
            ref_board[r1][c1] -= dg
            try:
                ref_board[r2+1][c1] += dg
            except IndexError:
                pass
            try:
                ref_board[r1][c2+1] += dg
            except IndexError:
                pass
            try:
                ref_board[r2+1][c2+1] -= dg
            except IndexError:
                pass
        else:
            ref_board[r1][c1] += dg
            try:
                ref_board[r2+1][c1] -= dg
            except IndexError:
                pass
            try:
                ref_board[r1][c2+1] -= dg
            except IndexError:
                pass
            try:
                ref_board[r2+1][c2+1] += dg
            except IndexError:
                pass
    for i in range(r):
        for j in range(1,c):
            ref_board[i][j] += ref_board[i][j-1]
    for j in range(c):
        for i in range(1,r):
            ref_board[i][j] += ref_board[i-1][j]
    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] + ref_board[i][j] > 0:
                cnt += 1
    return cnt