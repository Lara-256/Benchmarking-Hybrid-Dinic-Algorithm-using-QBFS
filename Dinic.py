from collections import deque

def bfs(graph):

    V = len(graph)

    # level=-1
    level=[-1]*(V)
    queue=deque()

    # level(s)=0 and queue s

    level[0]=0
    queue.append(0)

    while len(queue)!=0:
        item=queue.popleft()
        for x in range(len(graph[item])):
            if graph[item][x] != 0 and level[x] == -1:
                level[x] = level[item] + 1
                queue.append(x)

    return level

def dfs(graph, level, u, flow, path, paths):

    V = len(graph)

    path.append(u)

    if u==V-1:
        paths.append((list(path),flow))
        path.pop()
        return flow

    totflow=0
    for  i in range(V):
        if graph[u][i]>0 and level[i]==level[u]+1:
            bottleneck = min(graph[u][i],flow)
            bottleneck2=dfs(graph,level,i,bottleneck,path,paths)

            if bottleneck2>0:
                graph[u][i] -= bottleneck2
                graph[i][u] += bottleneck2
                totflow += bottleneck2
                break

    path.pop()
    return totflow

def find_all_paths(graph, level):
    V = len(graph)
    paths = []
    totflow = 0

    while True:
        path = []
        flow = dfs(graph, level, 0, float('inf'), path, paths)
        if flow == 0:
            break
        totflow += flow

    return totflow, paths

def dynic(graph):

    V=len(graph)
    pathstaken=[]
    totalflow=0

    level = bfs(graph)
    while level[V-1]!=-1:
        list=find_all_paths(graph, level)
        flow=list[0]
        paths=list[1]
        totalflow+=flow
        pathstaken.extend(paths)
        level=bfs(graph)

    return totalflow,pathstaken


graph1=[[0,2,7,0,0,0],[0,0,0,9,0,0],[0,0,0,0,5,0],[0,0,0,0,9,5],[0,2,0,0,0,3],[0,0,0,0,0,0]]
graph2=[[0,11,7,10,0,0,0,0],[0,0,0,0,9,7,0,0],[0,1,0,6,0,1,0,0],[0,0,0,0,0,9,7,0],[0,0,0,0,0,0,0,7],[0,0,0,0,0,0,6,11],[0,0,0,0,0,0,0,12],[0,0,0,0,0,0,0,0]]
x=dynic(graph1)
print(x)
print(graph1)

y=dynic(graph2)
print(y)
print(graph2)


