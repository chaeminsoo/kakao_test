# 2021 KAKAO BLIND RECRUITMENT
d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.',]

def solution(new_id):
    ans = ''
    new_id = new_id.lower()
    for i in new_id:
        if i in d:
            if ans:
                if i == '.':
                    if ans[-1] == '.':
                        continue
                    else:
                        ans += i
                else:
                    ans+=i    
            else:
                if i == '.':
                    continue
                else:
                    ans+=i
        else: continue
    ans = ans[:15]
    if ans and ans[-1] == '.': ans = ans[:-1]
    if not ans: ans+='a'
    while len(ans) < 3:
        ans += ans[-1]
    return ans