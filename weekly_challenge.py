# insufficient amount of money
def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += i*price
    if money > answer:
        return 0
    else:
        return answer - money

# stars in meets
def solution(line):
    meets = []
    ll = len(line)
    for i in range(ll):
        for j in range(ll):
            if i == j: continue
            a,b,e = line[i]
            c,d,f = line[j]
            if (a*d) - (b*c) == 0: continue
            x = ((b*f)-(e*d))/((a*d)-(b*c))
            y = ((e*c)-(a*f))/((a*d)-(b*c))
            if x%1 == 0 and y%1 == 0:
                meets.append((int(x),int(y)))
    meets = list(set(meets))
    u = -1e15
    d = 1e15
    l = 1e15
    r = -1e15
    for i,j in meets:
        u = max(u,j)
        d = min(d,j)
        l = min(l,i)
        r = max(r,i)
    ans = [['.']*(r-l+1) for _ in range(u-d+1)]
    new_meets = []
    for i,j in meets:
        j = abs(u - j)
        i = abs(l - i)
        new_meets.append([j,i])
    for i,j in new_meets:
        ans[i][j] = '*'
    rslt = []
    for i in ans:
        rslt.append(''.join(i))
    return rslt