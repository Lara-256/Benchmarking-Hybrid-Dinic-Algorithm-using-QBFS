from collections import deque

#The following code shows the implementation of the BFS for creating a level graph.

def bfs(graph):

    V = len(graph) #number of nodes

    # level=-1
    level=[-1]*V
    queue=deque()

    # level(s)=0 and queue s
    level[0]=0
    queue.append(0)

    while len(queue)!=0:
        item=queue.popleft() #analyze first item of the queue
        for x in range(len(graph[item])):
            if graph[item][x]!=0 and level[x]==-1: #Is x an unleveled neighbor of the node?
                level[x]=level[item]+1 #level x
                queue.append(x) #add x to the queue

    return level


#An example of a graph leveling for the graph from fig 4.1 in the thesis. Delete the '#' to run it
#graph=[[0,10,15,7,0,0,0,0,0,0],[0,0,0,0,9,0,0,0,0,0],[0,0,0,0,6,15,0,0,0,0],[0,0,0,0,0,0,30,0,0,0],[0,0,0,0,0,0,0,4,0,0],[0,0,0,0,0,0,0,20,0,0],[0,0,0,0,0,0,0,0,27,0],[0,0,0,18,0,0,0,0,0,11],[0,0,0,0,0,0,0,0,0,25],[0,0,0,0,0,0,0,0,0,0]]

#leveling = bfs(graph)
#print("Levels:", leveling)
