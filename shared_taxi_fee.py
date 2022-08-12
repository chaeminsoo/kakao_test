def solution(n, s, a, b, fares):
    graph = [[int(1e9)]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
                
    for i,j,k in fares:
        graph[i-1][j-1] = k
        graph[j-1][i-1] = k
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])
    
    stnd = graph[s-1][b-1] + graph[s-1][a-1]
    for t in range(n):
        stnd = min(stnd,graph[s-1][t]+graph[t][b-1]+graph[t][a-1])
                
    return stnd