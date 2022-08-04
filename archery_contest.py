# 2022 KAKAO BLIND RECRUITMENT
from itertools import combinations_with_replacement

def solution(n, info):
    lion_shots = combinations_with_replacement([i for i in range(11)],n)
    cha = [0,[-1]*11]
    for i in lion_shots:
        lion = 0
        peach = 0
        l_info = [0]*11
        for j in i:
            l_info[10-j] += 1
        for k in range(11):
            if info[k] >= l_info[k] and info[k] != 0:
                peach += (10-k)
            elif info[k] < l_info[k]:
                lion += (10-k)
        if lion > peach:
            if cha[0] < lion-peach:
                cha[0] = lion-peach
                cha[1] = l_info
            elif cha[0] == lion-peach:
                for l in range(10,-1,-1):
                    if (l_info[l] - cha[1][l]) > 0:
                        cha[1] = l_info
                        break
                    elif (l_info[l] - cha[1][l]) < 0:
                        break
    if cha[1][0] == -1:
        return [-1]
    else:
        return cha[1]