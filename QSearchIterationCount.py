import numpy as np
import math

#The following code shows the implementation of the iteration count for finding one searched item of a list of t
#marked items in a search space of the size X. The calculation is done analytically.

def n(X,t):
    k_max=math.ceil(np.log(X/(2*np.sqrt(X-1))))+4 #k_max gives the number of iterations of each iteration of Grover's
    # algorithm
    theta=np.arcsin(np.sqrt(t/X))

    n_Q=0

    for k in range(1,k_max+1):
        m_k=math.floor(min(((6/5)**k),np.sqrt(X))) #m_k is the upper bound of repetitions of Grover's algorithm in the
        # k-th step of the algorithm

        prod=1
        for l in range(1,k): #This calculation gives the product within the sum to calculate n_Q
            m_l=math.floor(min(((6/5)**l),np.sqrt(X)))
            prod_part=0.5+(np.sin(4*(m_l+1)*theta))/(4*(m_l+1)*np.sin(2*theta))
            prod*=prod_part

        n_Q +=m_k/2*prod #Add the next term of the sum to n_Q

    return n_Q

#An example of a calculation of n_q with 2 marked items and a search space of the size 6. Delete the '#' to run it
#X=6
#t=2
#result=n(X,t)
#print("The results are:",result)