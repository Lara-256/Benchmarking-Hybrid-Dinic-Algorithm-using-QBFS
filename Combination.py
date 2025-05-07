import time

import random
from collections import deque
import numpy as np
import math

def randomgraph(v,p):
    graph = {i: [] for i in range(1, v + 1)}  # 1-based indexing

    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i!=j and random.random() < p:
                graph[i].append(j)

    return graph

def bfs(graph):

    V = len(graph)

    # level=-1
    level=[-1]*(V)
    queue=deque()

    # level(s)=0 and queue s

    level[0]=0
    queue.append(1)

    while len(queue)!=0:
        item=queue.popleft()
        for x in graph[item]:
            if level[x-1]==-1:
                level[x-1]=level[item-1]+1
                queue.append(x)
    return level

end=time.time()

def n(graph):
    V = len(graph)
    t = len(graph[1])

    k_max=math.ceil(np.log(V/(2*np.sqrt(V-1))))+4
    theta=np.arcsin(np.sqrt(t/V))

    n_Q=0

    for k in range(1,k_max+1):
        m_k=math.floor(min(((6/5)**k),np.sqrt(V)))

        prod=1
        for l in range(1,k):
            m_l=math.floor(min(((6/5)**l),np.sqrt(V)))
            prod_part=0.5+(np.sin(4*(m_l+1)*theta))/(4*(m_l+1)*np.sin(2*theta))
            prod*=prod_part

        n_Q +=m_k/2*prod

    return n_Q

rg=randomgraph(100,0.01)
print('The graph is:', rg)

start = time.time()

leveling = bfs(rg)

end=time.time()

print("The levels are given as:", leveling)

nQ=n(rg)
print("The results for n_Q are:",nQ)

timepast=end-start
print('The process time is ',timepast,' seconds')