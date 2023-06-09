import numpy as np
pip install cvxpy
import cvxpy as cp

#We'll first define the phase retrieval problem using the PhaseLift method. 

def pr(b, a, W): 
    m = len(b)
    n= len(a[0])
    X = cp.Variable((n,n), symmetric=True)
    constraints = [X >> 0]
    constraints += [cp.trace(a[i]@(a[i].T) @ X) == b[i] for i in range(m)]
    prob = cp.Problem(cp.Minimize(cp.trace(W @ X)), constraints)
    prob.solve()
    # print("The optimal value is", prob.value)
    return X.value
    
    W0 = pr(b,a,W) #this defined the solution to the problem when W is the identity matrix. 
    
    #Now, we'll define the PhaseLift method using a trace minimization problem with weighted matrices. 
    
    def itpr(b,a,eps,k):
    W=np.eye(len(a[0]))
    for i in range(k):
        X=pr(b,a,W)
        # print(X)
        W=np.linalg.inv(X+eps*np.eye(len(a[0])))
    return(X)
    
    #This returns the optimal solution X, matrix, to the phase retrieval problem. 
    
