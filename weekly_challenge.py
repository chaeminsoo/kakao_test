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
    u = -1e9
    d = 1e9
    l = 1e9
    r = -1e9
    for i,j in meets:
        u = max(u,j)
        d = min(d,j)
        l = min(l,i)
        r = max(r,i)
    print(meets)
    print(u,d,l,r)
    ans = [['.']*(r-l+1) for _ in range(u-d+1)]
    
            
    
            
            
    return ans




