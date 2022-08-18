# 2021 Kakao Recruiting Internship
from collections import deque

def solution(n, k, cmd):
    ans = ''
    cursor_ = k
    stnd_list = ['a'*i for i in range(1,n+1)]
    ref_list = ['a'*i for i in range(1,n+1)]
    dump = deque()
    for i in cmd:
        if len(i) > 1:
            a,b = i.split()
            if a == 'U': cursor_ -= int(b)
            else: cursor_ += int(b)
        else:
            if i == 'C':
                dump.append([cursor_,ref_list[cursor_]])
                del ref_list[cursor_]
                try:
                    c = ref_list[cursor_]
                except IndexError:
                    cursor_ -= 1
            else:
                idx, val = dump.popleft()
                ref_list.insert(idx,val)
    
    stp = 0
    rfp = 0
    while stp < n:
        if stnd_list[stp] == ref_list[rfp]:
            ans += 'O'
            stp+=1
            rfp+=1
        else:
            ans+='X'
            stp+=1
    print('s:',stnd_list)
    print('r:',ref_list)
              
    return ans