# lotto best worst: Greedy

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    znt = 0
    for i in lottos:
        if i in win_nums:
            cnt+=1
        elif i == 0:
            znt+=1
    ans = [6,6,5,4,3,2,1]
    answer.append(ans[cnt+znt])
    answer.append(ans[cnt])
    return answer

# matrix rotate: Basic

def solution(rows, columns, queries):
    answer = []
    board = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt+=1
            
    for i in queries:
        rslt = 1e9
        u,d,l,r = i[0]-1, i[2]-1, i[1]-1, i[3]-1
        ref = board[u][l]
        rslt = min(ref,rslt)
        for j in range(u,d):
            board[j][l] = board[j+1][l]
            rslt = min(board[j][l],rslt)
        for j in range(l,r):
            board[d][j] = board[d][j+1]
            rslt = min(board[d][j],rslt)
        for j in range(d,u,-1):
            board[j][r] = board[j-1][r]
            rslt = min(board[j][r],rslt)
        for j in range(r,l,-1):
            board[u][j] = board[u][j-1]
            rslt = min(board[u][j],rslt)
        board[u][l+1] = ref
        answer.append(rslt)
    return answer

# multilevel tooth brash sale : Dictionary

def solution(enroll, referral, seller, amount):
    bene = {}
    whos_superiors = {}
    for i, j in enumerate(enroll):
        bene[j] = 0
        whos_superiors[j] = referral[i]
    
    def mny_up(st,mny):
        sang_nab = int(mny*0.1)
        if sang_nab == 0:
            bene[st] += mny
            return
        if whos_superiors[st] == '-':
            bene[st] += mny-sang_nab
            return
        
        bene[st] += mny-sang_nab
        mny_up(whos_superiors[st],sang_nab)
    
    for i,j in enumerate(seller):
        mny = amount[i]*100
        mny_up(j,mny)
        
    return list(bene.values())