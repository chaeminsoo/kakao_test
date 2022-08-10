# 2021 KAKAO BLIND RECRUITMENT
from bisect import bisect_left

def checking(cjp,bf,js,cp,ref):
    cnt = 0
    if cjp == '-' or cjp == ref[1]:
        cnt+=1
    if bf == '-' or bf == ref[2]:
        cnt+=1
    if js == '-' or js == ref[3]:
        cnt+=1
    if cp == '-' or cp == ref[4]:
        cnt+=1
    if cnt >= 4:
        return True
    else:
        return False

def solution(info, query):
    answer = []
    new_info = []
    for i in info:
        j,k,l,m,n = i.split()
        new_info.append([int(n),j,k,l,m])
    new_info.sort()
    for i in query:
        cjp,a,bf,b,js,c,cp,num = i.split()
        num = int(num)
        idx = bisect_left(new_info,[num])
        cnt = 0
        for j in new_info[idx:]:
            if checking(cjp,bf,js,cp,j):
                cnt+=1
        answer.append(cnt)
    return answer
#=============================================================================
from bisect import bisect_left

def solution(info, query):
    answer = []
    new_info = {
        'java':{
            'backend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            'frontend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            '-':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}}
        },
        'python':{
            'backend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            'frontend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            '-':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}}
        },
        'cpp':{
            'backend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            'frontend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            '-':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}}
        },
        '-':{
            'backend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            'frontend':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}},
            '-':{'-':{'pizza':[], 'chicken':[], '-':[]}, 'junior':{'pizza':[], 'chicken':[], '-':[]}, 'senior':{'pizza':[], 'chicken':[], '-':[]}}
        }
               }
    for i in info:
        cjp, bf,js,cp,num = i.split()
        for ii in ['-',cjp]:
            for jj in ['-', bf]:
                for kk in ['-',js]:
                    for ll in ['-',cp]:
                        new_info[ii][jj][kk][ll].append(int(num))
                        
    for i in query:
        cjp ,a, bf ,b, js ,c, cp , num = i.split()
        num = int(num)
        new_info[cjp][bf][js][cp].sort()
        idx_1 = bisect_left(new_info[cjp][bf][js][cp],num)
        idx_2 = bisect_left(new_info[cjp][bf][js][cp],200000)
        answer.append(idx_2-idx_1)
    return answer