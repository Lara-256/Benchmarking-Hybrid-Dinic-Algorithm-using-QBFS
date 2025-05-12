from weakref import finalize


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
            bottleneck2 = dfs(graph, level, i, bottleneck, path, paths)
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
        path1 = []
        flow = dfs(graph, level, 0, float('inf'), path1, paths)
        totflow+=flow
        if flow == 0:
            break

    return totflow,paths




graph1=[[0,2,7,0,0,0],[0,0,0,9,0,0],[0,0,0,0,5,0],[0,0,0,0,9,5],[0,2,0,0,0,3],[0,0,0,0,0,0]]
leveling=[0,1,1,2,2,3]

graph2=[[0,11,7,10,0,0,0,0],[0,0,0,0,9,7,0,0],[0,1,0,6,0,1,0,0],[0,0,0,0,0,9,7,0],[0,0,0,0,0,0,0,7],[0,0,0,0,0,0,6,11],[0,0,0,0,0,0,0,12],[0,0,0,0,0,0,0,0]]
leveling2=[0, 1, 1, 1, 2, 2, 2, 3]

x=find_all_paths(graph1, leveling)
print(x)
print(graph1)

y=find_all_paths(graph2, leveling2)
print(y)
print(graph2)