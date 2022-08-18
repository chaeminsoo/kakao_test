# 2021 Kakao Recruiting Internship

dx = [-2,2,0,0,-1,1,0,0,-1,1,1,-1]
dy = [0,0,-2,2,0,0,-1,1,1,1,-1,-1]

def distance_(x,y,d,room):
    if d in [4,5,6,7]:
        return False
    if d == 0:
        if room[x+dx[4]][y+dy[4]] == 'X': return True
        else: return False
    if d == 1:
        if room[x+dx[5]][y+dy[5]] == 'X': return True
        else: return False
    if d == 2:
        if room[x+dx[6]][y+dy[6]] == 'X': return True
        else: return False
    if d == 3:
        if room[x+dx[7]][y+dy[7]] == 'X': return True
        else: return False
    if d == 8:
        if room[x+dx[4]][y+dy[4]] =='X' and room[x+dx[7]][y+dy[7]] =='X': return True
        else: return False
    if d == 9:
        if room[x+dx[5]][y+dy[5]] =='X' and room[x+dx[7]][y+dy[7]] =='X': return True
        else: return False
    if d == 10:
        if room[x+dx[5]][y+dy[5]] =='X' and room[x+dx[6]][y+dy[6]] =='X': return True
        else: return False
    if d == 11:
        if room[x+dx[6]][y+dy[6]] =='X' and room[x+dx[4]][y+dy[4]] =='X': return True
        else: return False

def solution(places):
    answer = []
    for ii,room in enumerate(places):
        r_sw = False
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    for k in range(12):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < 5 and 0 <= ny < 5 and room[nx][ny] == 'P':
                            if distance_(i,j,k,room):
                                pass
                            else:
                                r_sw = True
                                break
                    if r_sw:
                        break
            if r_sw:
                    break
        if r_sw:
            answer.append(0)
        else:
            answer.append(1)
    return answer