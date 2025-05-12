import time

import random
from random import randrange
from collections import deque
import numpy as np
import math

def randomgraph(v,p):
    graph = [[0] * v for i in range(v)]  # 1-based indexing

    for i in range(v):
        for j in range(i+1,v):
            if random.random() < p:
                graph[i][j] = randrange(1, 10)

    return graph

def bfs(graph):

    V = len(graph)

    # level=-1
    level = [-1] * V
    queue = deque()

    # level(s)=0 and queue s

    level[0] = 0
    queue.append(0)

    while len(queue) != 0:
        item = queue.popleft()
        for x in range(len(graph[item])):
            if graph[item][x] != 0 and level[x] == -1:
                level[x] = level[item] + 1
                queue.append(x)

    return level

def n(graph):
    V = len(graph)
    t = np.count_nonzero(graph[1])

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

rg=randomgraph(100,0.5)
print('The graph is:', rg)

start = time.time()

leveling = bfs(rg)

end=time.time()

print("The levels are given as:", leveling)

nQ=n(rg)
print("The results for n_Q are:",nQ)

timepast=end-start
print('The process time is ',timepast,' seconds')