from collections import deque
import numpy as np
import math
import time
import random
from random import randrange
import pandas as pd

#The following code shows the comparison of the BFS algorithm and the results of the iteration count for a random graph.
#The algorithm runs the whole Dinic's algorithm. Also, it shows how many iterations of Grover's algorithm are needed
#when using the QBFS on this graph in the quantum algorithm.

#The individual codes are explained in their own files.

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

def dfs_find_all_paths(graph, level):
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

def n(X,t):
    if X<=1:
        return 1

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


#This is the main part of Dinic's algorithm.
def dynic(graph):

    V=len(graph)
    pathstaken=[] #reset all variables
    totalflow=0
    bfstime = 0

    start = time.time() #run the first iteration to level a graph using the BFS and measure the time
    level = bfs(graph)
    end = time.time()

    bfstime+=end-start #add the time to the overall BFS time

    #calculate how many iterations the leveling would take using the QBFS
    levelindex=1        #gives on which level we are working
    qbfsiterations=0          #number of iterations
    X=V-1               #number of not leveled vertices
    vertexperlvl=[1]    #vertices in level 0 are always 1 (only s)
    vertexperlvl.append(level.count(levelindex))    #vertices in level 1
    t=vertexperlvl[levelindex]      #vertices in level we are working on

    #check that we have vertices in the level, if not we are finished
    while vertexperlvl[-1]!=0:
        #if X<=1 we have .../(X-1) which gives us impossible results
        if vertexperlvl[-1]>1:
            while t!=0:
                #calculate n_Q and update the number of vertices which aren't leveled yet
                n_Q=n(X,t)
                qbfsiterations+=math.ceil(n_Q) #add n_Q to the total iteration count
                X-=1
                t-=1
        elif vertexperlvl[-1]==1:
            qbfsiterations+=1 #the last step needs one iteration (O(1))
        #increase the level and update everything
        levelindex+=1
        vertexperlvl.append(level.count(levelindex))
        t=vertexperlvl[levelindex]

    #repeat the dfs and bfs until the end vertex can't be reached (level=-1)
    while level[V-1]!=-1:
        #find the paths and calculate the flow and define the paths taken
        list=dfs_find_all_paths(graph, level)
        flow=list[0]
        paths=list[1]
        #update the flow and the paths
        totalflow+=flow
        pathstaken.extend(paths)
        #new leveling after dfs
        start=time.time()
        level=bfs(graph)
        end = time.time()

        bfstime += end - start

        #repeat the QBFS iteration count calculation for the new leveling
        levelindex = 1
        X = V - 1
        vertexperlvl = [1]
        vertexperlvl.append(level.count(levelindex))
        t = vertexperlvl[levelindex]
        while vertexperlvl[-1] != 0:
            if vertexperlvl[-1] > 1:
                while t != 0:
                    n_Q = n(X, t)
                    qbfsiterations += math.ceil(n_Q)
                    X -= 1
                    t -= 1
            elif vertexperlvl[-1] == 1:
                qbfsiterations += 1
            levelindex += 1
            vertexperlvl.append(level.count(levelindex))
            t = vertexperlvl[levelindex]



    return totalflow,pathstaken,qbfsiterations,bfstime #return the flow, the paths, the QBFS iteration count and the
    # BFS time

def randomgraph(n,p):
    graph = [[0]*n for i in range(n)]  # 1-based indexing

    for i in range(n):
        for j in range(n):
            if i<j and random.random() < p:
                graph[i][j]=randrange(1,10)

    return graph

#run the hybrid benchmarking algorithm for random generated graphs with n nodes and a edge probability of p
def run_experiments(n_values, p_values):
    results = []
    for n in n_values:
        for p in p_values:
            graph=randomgraph(n,p) #generate a random graph
            dyn=dynic(graph) #run Dinic's algorithm
            classical_time=dyn[3] #filter the BFS time and the QBFS iteration count from thr results
            quantum_steps=dyn[2]
            threshold_gate=classical_time / (quantum_steps*(4*math.ceil(math.log2(n))+1)) if quantum_steps != 0 else None
            #calculate the threshold gate time
            results.append({ #ouput
                'Vertices (n)': n,
                'Edge Prob. (p)': p,
                'BFS Time (s)': classical_time,
                'Quantum BFS Iterations': quantum_steps,
                'Threshold Gate Time': threshold_gate
            })
    return pd.DataFrame(results)

#The results were obtained using the following command. The calculation was repeated five times.
#Delete the '#' to run them

#nvalsparse=[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600]
#vvalsparse=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
#resultssparse=run_experiments(nvalsparse,vvalsparse)
#print(resultssparse)
#resultssparse.to_csv("experiment_results.csv", index=False)

#nvaldense=[100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
#vvaldense=[0.70,0.72,0.74,0.76,0.78,0.80,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98]
#resultsdense=run_experiments(nvaldense,vvaldense)
#print(resultsdense)
#resultsdense.to_csv("experiment_results.csv", index=False)