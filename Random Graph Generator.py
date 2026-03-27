import random
from random import randrange

#The following code shows the creation of a pseudo-random graph.

def randomgraph(n,p):
    graph = [[0]*n for i in range(n)]  # create a n x n Matrix containing only 0's

    for i in range(n):
        for j in range(n):
            if i<j and random.random() < p: #For each pair of nodes (i,j), an edge is created with a probability p
                graph[i][j]=randrange(1,10) #The edges have a capacity randomly assigned between 1 and 10

    return graph


#An example of a graph generation with n=600 and an edge probability of 10%. Delete the '#' to run it
#rg=randomgraph(600,0.1)
#print(rg)