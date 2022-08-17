from itertools import permutations
from collections import deque

def find_card(board):
    ref = {}
    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0 and num in ref:
                ref[num].append([i,j])
            else:
                ref[num] = [[i,j]]            
    return ref

rp = []
def r_plan(num,pl):
    global rp
    if len(pl) == num:
        rp.append(pl)
        return
    r_plan(num,pl+'0')
    r_plan(num,pl+'1')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def remove_one(r,c,num,o,clocs,board):
    visited = [[False]*4 for _ in range(4)]
    range_board = [[0]*4 for _ in range(4)]
    q = deque()
    q.append([r,c,0])
    visited[r][c] = True
    while q:
        x,y,v = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                q.append([nx,ny,v+1])
                range_board[nx][ny] = v+1
                visited[nx][ny] = True
            
            while 0 <= nx < 4 and 0 <= ny < 4:
                nx += dx[i]
                ny += dy[i]
                
                if board[nx][ny] != 0 and not visited[nx][ny]:
                    q.append([nx,ny,v+1])
                    range_board[nx][ny] = v+1
                    visited[nx][ny] = True
    
                    
                
                
            
            
            
            
    return r,c,cnt
    

def remove_card(r,c,board,ordr,rp,clocs):
    for i in range(len(ordr)):
        remove_one(r,c,ordr[i],rp[i],clocs)
    
    
    
    return
    
                                
def solution(board, r, c):
    ans = 1e9
    cards = []
    cards_loc = find_card(board)
    big_card = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.append([board[i][j],i,j])
                big_card = max(big_card,board[i][j])
    ref_cards = [i for i in range(1,big_card+1)]
    orders = list(permutations(ref_cards,len(ref_cards)))
    for i in orders:
        r_plan(big_card,'')
        for j in rp:
            ans = min(remove_card(r,c,board,i,j,cards_loc),ans)
        rp.clear()
        
        
            
            
            
        
    
            
            
    return ans




