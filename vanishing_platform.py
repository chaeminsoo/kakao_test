dx = [-1,1,0,0]
dy = [0,0,-1,1]

a_win = []
b_win = []
def dfs(board,a,b,ant,bnt,t,r,c):
    global a_win, b_win
    if board[a[0]][a[1]] == 0:
        b_win.append((ant,bnt,ant+bnt))
        return #(ant,bnt,ant+bnt)
    elif board[b[0]][b[1]] == 0:
        a_win.append((ant,bnt,ant+bnt))
        return #(ant,bnt,ant+bnt)
    
    if t == 0: #a
        x,y = a[0],a[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                board[x][y] = 0
                a = [nx,ny]
                dfs(board,a,b,ant+1,bnt,1,r,c)
                a = [x,y]
                board[x][y] = 1
    elif t == 1: #b
        x,y = b[0],b[1]
        for i in range(4):
            # dnt=0
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 0:
                board[x][y] = 0
                b = [nx,ny]
                dfs(board,a,b,ant,bnt+1,0,r,c)
                b = [x,y]
                board[x][y] = 1
            # else:
            #     dnt+=1
        # if dnt >= 4:
                

def solution(board, aloc, bloc):
    r = len(board)
    c = len(board[0])
    dfs(board,aloc,bloc,0,0,0,r,c)
    a_win.sort(key = lambda x:(x[0],-x[1]))
    b_win.sort(key = lambda x:(x[1],-x[0]))
    if a_win and b_win:
        rslt_a = a_win[0]
        rslt_b = b_win[0]
        if rslt_a[0] > rslt_b[1]:
            print(rslt_a,'//b', rslt_b) #
            return rslt_b[2]
        elif rslt_a[0] < rslt_b[1]:
            print(rslt_a,'//a', rslt_b) #
            return rslt_a[2]
        elif rslt_a[0] == rslt_b[1]:
            if rslt_a[1] > rslt_b[0]:
                print(rslt_a,'//a', rslt_b) #
                return rslt_a[2]
            elif rslt_a[0] < rslt_b[1]:
                print(rslt_a,'//b', rslt_b) #
                return rslt_b[2]
    elif not a_win and b_win:
        print(b_win,'//b') #
        return b_win[0][2]
    elif a_win and not b_win:
        print(a_win,'//a') #
        return a_win[0][2]
    elif not a_win and not b_win:
        return 0
    