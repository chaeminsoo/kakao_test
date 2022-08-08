answer = 0
def dfs(now,s,w,visited,info,edge):
    global answer
    if info[now] == 0:
        s+=1
    elif info[now] == 1:
        w+=1
    else: pass

    if s <= w: return
    else: answer = max(answer,s)
    
    for i in edge[now]:
        if not visited[i][s][w]:
            ref = info[now]
            info[now] = -1
            visited[now][s][w] = True
            dfs(i,s,w,visited,info,edge)
            visited[now][s][w] = False
            info[now] = ref
    return

def solution(info, edges):
    global answer
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
    dfs(0,0,0,visited,info,edge)
    return answer