import random

def randomgraph(n,p):
    graph = {i: [] for i in range(1, n + 1)}  # 1-based indexing

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i!=j and random.random() < p:
                graph[i].append(j)

    return graph

rg=randomgraph(100,0.1)
print(rg)