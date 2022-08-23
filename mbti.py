# 2022 kakao tech internship
def score(c,y,n):
    if c == 1: return n, 3
    if c == 2: return n, 2
    if c == 3: return n, 1
    if c == 4: return n, 0
    if c == 5: return y, 1
    if c == 6: return y, 2
    if c == 7: return y, 3

def solution(survey, choices):
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    for i in range(len(survey)):
        n,y = survey[i][0], survey[i][1]
        c = choices[i]
        r1, r2 = score(c,y,n)
        mbti[r1] += r2
    for i,j in [['R','T'], ['C','F'], ['J','M'], ['A', 'N']]:
        if mbti[i] > mbti[j]:
            answer += i
        elif mbti[i] == mbti[j]:
            ref = [i,j]
            ref.sort()
            answer+=ref[0]
        else:
            answer += j
    return answer