# 2021 KAKAO BLIND RECRUITMENT
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        ref = []
        for j in orders:
            combis = list(combinations(j,i))
            for k in combis:
                ref.append(set(k))
        ref_with_num = []
        for j in ref:
            k = ref.count(j)
            if k >= 2:
                ref_with_num.append([k,j])
        ref_with_num.sort()        
        if ref_with_num:
            ref_num = ref_with_num[-1][0]
            while ref_with_num:
                n,com = ref_with_num.pop()
                if n != ref_num:
                    break
                else:
                    com = list(com)
                    com.sort()
                    l = ''.join(com)
                    answer.append(l)
                    ref_num = n
    answer = list(set(answer))
    answer.sort()
    return answer