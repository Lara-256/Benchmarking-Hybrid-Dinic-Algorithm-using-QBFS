from collections import deque

def bfs(graph):

    V = len(graph)

    # level=-1
    level=[-1]*V
    queue=deque()

    # level(s)=0 and queue s

    level[0]=0
    queue.append(0)

    while len(queue)!=0:
        item=queue.popleft()
        for x in range(len(graph[item])):
            if graph[item][x]!=0 and level[x]==-1:
                level[x]=level[item]+1
                queue.append(x)

    return level



graph=[[0,2,7,0,0,0],[0,0,0,9,0,0],[0,0,0,0,5,0],[0,0,0,0,9,5],[0,2,0,0,0,3],[0,0,0,0,0,0]]
graph2=[[0,11,7,10,0,0,0,0],[0,0,0,0,9,7,0,0],[0,1,0,6,0,1,0,0],[0,0,0,0,0,9,7,0],[0,0,0,0,0,0,0,7],[0,0,0,0,0,0,6,11],[0,0,0,0,0,0,0,12],[0,0,0,0,0,0,0,0]]

leveling = bfs(graph2)
print("Levels:", leveling)
