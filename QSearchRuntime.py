import numpy as np
import math

def n(X,t):
    k_max=math.ceil(np.log(X/(2*np.sqrt(X-1))))+4
    theta=np.arcsin(np.sqrt(t/X))

    n_Q=0

    for k in range(1,k_max+1):
        m_k=math.floor(min(((6/5)**k),np.sqrt(X)))

        prod=1
        for l in range(1,k):
            m_l=math.floor(min(((6/5)**l),np.sqrt(X)))
            prod_part=0.5+(np.sin(4*(m_l+1)*theta))/(4*(m_l+1)*np.sin(2*theta))
            prod*=prod_part

        n_Q +=m_k/2*prod

    return n_Q

X=6
t=2
result=n(X,t)
print("The results are:",result)

def dfs(graph, level, u, flow, path, paths):
    V = len(graph)

    # Add the current node to the path
    path.append(u)

    # If we've reached the sink node, add the current path to paths and return the flow
    if u == V - 1:
        paths.append((list(path), flow))
        path.pop()
        return flow

    totflow = 0
    for i in range(V):
        # Only consider edges that are still available (positive capacity) and follow the level rule
        if graph[u][i] > 0 and level[i] == level[u] + 1:
            bottleneck = min(graph[u][i], flow)
            bottleneck2 = dfs(graph, level, i, bottleneck, path, paths)
            if bottleneck2 > 0:
                # Adjust flow in the residual graph
                graph[u][i] -= bottleneck2
                graph[i][u] += bottleneck2
                totflow += bottleneck2

    # After exploring all edges, pop the current node from the path
    path.pop()

    return totflow

def find_all_paths(graph, level):
    V = len(graph)
    paths = []
    while True:
        path1 = []
        flow = dfs(graph, level, 0, float('inf'), path1, paths)
        if flow == 0:
            break  # No more augmenting paths found
    return paths

# Test the function
graph2 = [
    [0, 11, 7, 10, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 7, 0, 0],
    [0, 1, 0, 6, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 9, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 6, 11],
    [0, 0, 0, 0, 0, 0, 0, 12],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

leveling2 = [0, 1, 1, 1, 2, 2, 2, 3]

paths = find_all_paths(graph2, leveling2)
print(paths)
print(graph2)
