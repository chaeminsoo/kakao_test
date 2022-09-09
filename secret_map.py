# 2018 kakao blind recruitment
def mdnum(num,n):
    word=""
    while num:
        word = str(num%n)+word
        num=num//n
    return word

def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    m1 = []
    m2 = []
    for i in arr1:
        ref = mdnum(i,2)
        if len(ref) < n:
            ref2 = n - len(ref)
            ref = '0'*ref2 + ref
        m1.append(ref)
    for i in arr2:
        ref = mdnum(i,2)
        if len(ref) < n:
            ref2 = n - len(ref)
            ref = '0'*ref2 + ref
        m2.append(ref)
    for i in range(n):
        for j in range(n):
            if m1[i][j] == '0' and m2[i][j] == '0':
                answer[i] += ' '
            else:
                answer[i] +='#'
    return answer