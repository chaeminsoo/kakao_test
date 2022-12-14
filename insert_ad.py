# 2021 KAKAO BLIND RECRUITMENT
def solution(play_time, adv_time, logs):
    h,m,s = play_time.split(':')
    play_time = int(h)*60*60 + int(m)*60 + int(s)
    h,m,s = adv_time.split(':')
    adv_time = int(h)*60*60 + int(m)*60 + int(s)
    time_line = [0]*(play_time+2)
    for i in logs:
        st,et = i.split('-')
        h,m,s = st.split(':')
        st = int(h)*60*60 + int(m)*60 + int(s)
        h,m,s = et.split(':')
        et = int(h)*60*60 + int(m)*60 + int(s)
        
        time_line[st] += 1
        time_line[et+1] -= 1
    p_sum = [0]*(play_time+2)
    for i in range(1,play_time+2):
        time_line[i] += time_line[i-1]
        p_sum[i] += time_line[i]
        p_sum[i] += p_sum[i-1]
    
    ans = [0,0]
    p_sum.insert(0,0)
    for i in range(1,play_time+1):
        try:
            wt = p_sum[adv_time+i] - p_sum[i-1]
            if wt > ans[0]:
                ans[0] = wt
                ans[1] = i-1
        except IndexError:
            break
        
    rslt = ans[1]
    h = rslt//(60**2)     
    rslt %= (60**2)
    m = rslt//60
    rslt %= 60
    if h < 10: h = '0'+str(h)
    else: h = str(h)
    if m < 10: m = '0'+str(m)
    else: m = str(m)
    if rslt < 10: rslt = '0'+str(rslt)
    else: rslt = str(rslt)
        
    return h + ':' + m + ':' + rslt

# print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))