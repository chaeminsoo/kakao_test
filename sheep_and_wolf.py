def dfs(now,s,w,visited,info,edge):
    global answer
    if info[now] == 0:
        s+=1
    elif info[now] == 1:
        w+=1
    else:
        pass
    visited.append([now,s,w])
    cnt = 0
    for i in edge[now]:
        if [i,s,w] not in visited:
            dfs(i,s,w,visited,info,edge)
            cnt+=1
    if cnt == 0:
        answer = max(answer,s)
        return

def solution(info, edges):
    answer = 0
    li = len(info)
    edge = [[] for _ in range(li)]
    for i,j in edges:
        edge[i].append(j)
        edge[j].append(i)
    dfs(0,1,0,[],info,edge)
    return answer







