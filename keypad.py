# 2020 kakao internship
def dis(a,b):
    x,y = a
    r,c = b
    return abs(x-r) + abs(y-c)

def solution(numbers, hand):
    ans = ''
    d = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    l = '*'
    r = '#'
    for i in numbers:
        if i in [1,4,7]:
            l = i
            ans+='L'
        elif i in [3,6,9]:
            r = i
            ans+='R'
        else:
            loc = d[i]
            ldis = dis(loc,d[l])
            rdis = dis(loc,d[r])
            if ldis == rdis:
                if hand == 'right':
                    ans+='R'
                    r = i
                else:
                    ans+='L'
                    l = i
            elif ldis > rdis:
                ans+='R'
                r = i
            else:
                ans+='L'
                l = i
    return ans