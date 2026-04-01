#The following code shows the implementation of the DFS for finding augmenting paths.

def dfs(graph, level, u, flow, path, paths):
#graph: residual graph in form of a matrix, level: level graph in form of a list, u: current node,
# flow: current bottleneck capacity, path: current path, paths: list of found paths

    V = len(graph) #number of nodes

    path.append(u) #add current node to the path

    if u==V-1: #if sink is reached, store the path and the flow
        paths.append((list(path),flow))
        path.pop()
        return flow

    totflow=0
    for  i in range(V):
        if graph[u][i]>0 and level[i]==level[u]+1: #explore neighbors with remaining capacity and a higher level
            bottleneck = min(graph[u][i],flow) #update the bottleneck capacity
            bottleneck2 = dfs(graph, level, i, bottleneck, path, paths) #recursively try to push the flow further
            if bottleneck2>0: #update the capacities to create the residual graph
                graph[u][i] -= bottleneck2
                graph[i][u] += bottleneck2
                totflow += bottleneck2 #store the current bottleneck capacity of the path
                break #stop if the search is successful

    path.pop() #backtrack
    return totflow


def find_all_paths(graph, level):
#repeatedly find augmenting paths until no more flow can be pushed through the level graph

    V = len(graph)
    paths = [] #store all augmenting paths
    totflow = 0

    while True:
        path1 = [] #reset path for each DFS
        flow = dfs(graph, level, 0, float('inf'), path1, paths) #find augmenting paths starting at the source s
        totflow+=flow #add the flow through a path to the total flow
        if flow == 0: #stop if no augmenting path can be found
            break

    return totflow,paths



#An example of a graph leveling for the graph from fig 4.1 in the thesis. Delete the '#' to run it
#graph1=[[0,10,15,7,0,0,0,0,0,0],[0,0,0,0,9,0,0,0,0,0],[0,0,0,0,6,15,0,0,0,0],[0,0,0,0,0,0,30,0,0,0],[0,0,0,0,0,0,0,4,0,0],[0,0,0,0,0,0,0,20,0,0],[0,0,0,0,0,0,0,0,27,0],[0,0,0,18,0,0,0,0,0,11],[0,0,0,0,0,0,0,0,0,25],[0,0,0,0,0,0,0,0,0,0]]
#leveling=[0, 1, 1, 1, 2, 2, 2, 3, 3, 4]

#x=find_all_paths(graph1, leveling)
#print(x)
#print(graph1)