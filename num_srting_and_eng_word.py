# 2021 Kakao Recruiting Internship

def solution(s):
    ans = []
    nums = ['0','1','2','3','4','5','6','7','8','9']
    sn = {'zero':'0','one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    ref = ''
    for i in s:
        if i in nums:
            ans.append(i)
        else:
            ref += i
        if ref in sn:
            ans.append(sn[ref])
            ref = ''
    return int(''.join(ans))