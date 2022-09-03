# 2022 kakao tech internship
def solution(alp, cop, problems):
    almx = 0
    comx = 0
    for i in problems:
        almx = max(i[0],almx)
        comx = max(i[1],comx)
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    problems.sort()
    dp = [[1e9]*(comx+2) for _ in range(almx+2)]
    for i in range(alp+1):
        for j in range(cop+1):
            dp[i][j] = 0
    for i in range(alp,almx+1):
        for j in range(cop,comx+1):
            for k in problems:
                if i >= k[0] and j >= k[1]:
                    try:
                        dp[i+k[2]][j+k[3]] = min(dp[i+k[2]][j+k[3]],dp[i][j] + k[4])
                    except IndexError:
                        pass
    
    return dp[almx][comx]

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))