import random
from random import randrange

def randomgraph(n,p):
    graph = [[0]*n for i in range(n)]  # 1-based indexing

    for i in range(n):
        for j in range(n):
            if i<j and random.random() < p:
                graph[i][j]=randrange(1,10)

    return graph

rg=randomgraph(100,0.8)
print(rg)