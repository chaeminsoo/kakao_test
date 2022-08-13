# 2021 KAKAO BLIND RECRUITMENT
from itertools import permutations

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









