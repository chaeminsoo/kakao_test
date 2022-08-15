# 2021 KAKAO BLIND RECRUITMENT
from itertools import permutations
from collections import deque

def find_card(n):
    ref = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == n:
                ref.append([i,j])
    return ref

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def remove_card(board,cloc,aloc,bloc):
    ref_b = [i[:] for i in board]
    ans = 1e9
    x,y = cloc
    for st, ed in [[aloc, bloc], [bloc, aloc]]:
        
        for i, j in [[cloc, st], [st, ed]]:
            r,c = i
            q = deque()
            q.append([r,c,0])
            visited = [[False]*4 for _ in range(4)]
            range_board = [[0]*4 for _ in range(4)]
            while q:
                x,y,v = q.popleft()
                range_board[x][y] = v
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                        if ref_b[nx][ny] != 0 and ref_b[x][y] == 0:
                            q.append([nx,ny,1 if v == 0 else v])
                            
def solution(board, r, c):
    answer = 0
    cards = []
    big_card = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.append([board[i][j],i,j])
                big_card = max(big_card,board[i][j])
    ref_cards = [i for i in range(1,big_card+1)]
    orders = list(permutations(ref_cards,len(ref_cards)))
    print(orders)
            
            
    return answer