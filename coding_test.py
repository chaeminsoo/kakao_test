# 2022 kakao tech internship
def solution(alp, cop, problems):
    almx = 0
    comx = 0
    for i in problems:
        almx = max(i[0],almx)
        comx = max(i[1],comx)
    
    dp = [[1e9]*(151) for _ in range(151)]
    for i in range(alp+1):
        for j in range(cop+1):
            dp[i][j] = 0
    for i in range(almx+1):
        for j in range(comx+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for k in problems:
                if i >= k[0] and j >= k[1]:
                    try:
                        dp[i+k[2]][j+k[3]] = min(dp[i+k[2]][j+k[3]],dp[i][j] + k[4])
                    except IndexError:
                        pass
                    
    
    return dp[almx][comx]