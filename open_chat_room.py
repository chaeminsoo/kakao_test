# 2019 kakao blind recruitment
def solution(record):
    answer = []
    ewords = '님이 들어왔습니다.'
    lwords = '님이 나갔습니다.'
    d = {}
    rslt = []
    for i in record:
        try:
            ordr, uid, nick = i.split()
        except ValueError:
            ordr, uid = i.split()
            rslt.append([uid,1])
        if ordr == 'Enter':
            d[uid] = nick
            rslt.append([uid,0])
        elif ordr == 'Change':
            d[uid] = nick
    for i in rslt:
        uid, io = i
        if io == 0:
            answer.append(d[uid]+ewords)
        else:
            answer.append(d[uid]+lwords)
    return answer