def dfs(now,s,w,visited,info,edge):
    global answer
    if s != 0 and s <= w:
        return
    
    if info[now] == 0: s+=1
    elif info[now] == 1: w+=1
    else: pass
    info[now] = -1
    print('==',s,'/',w,'/',info[now],now)
    visited[now][s][w] = True
    for i in edge[now]:
        if visited[i][s][w] == False:
            dfs(i,s,w,visited,info,edge)
    answer = max(answer,s)
    print('++',answer)
    return

def solution(info, edges):
    global answer
    answer = 0
    s_num = 0
    w_num = 0
    for i in info:
        if i ==0: s_num+=1
        else: w_num+=1
    edge = [[] for _ in range(s_num+w_num)]
    for i,j in edges:
        edge[i].append(j)
        edge[j].append(i)
    visited = [[[False]*(w_num+1) for i in range(s_num+1)] for j in range(s_num+w_num)]
    # for i in visited:
    #     print(i)
    dfs(0,0,0,visited,info,edge)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))