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
                        idx_0 = bisect_left(new_info[ii][jj][kk][ll],int(num))
                        new_info[ii][jj][kk][ll].insert(idx_0,int(num))
                        
    for i in query:
        cjp ,a, bf ,b, js ,c, cp , num = i.split()
        num = int(num)
        idx_1 = bisect_left(new_info[cjp][bf][js][cp],num)
        idx_2 = bisect_left(new_info[cjp][bf][js][cp],200000)
        answer.append(idx_2-idx_1)
    return answer