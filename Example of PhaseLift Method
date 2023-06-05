#We focused on implementing the PhaseLift method using a frame-theoretic approach. This is an example of using PhaseLift where part of the input is the frame coefficients constructed from a full spark frame and randomly generated vector x. 
#The output of this example of a rank-3 matrix. 

b=np.array([0.2994*0.2294, 0.3455*0.3455, 1.1124*1.1124, 0.3081*0.3081, 1.159*1.159]) #magnitude of frame cofficients 

a=[[0,0,1],[1,0,1],[0,1,1], [1, 1-np.sqrt(2), 2], [1,1,1]]
a = [np.array(x).reshape(3,1) for x in a]
a 
#above is full spark frame in R^3. 

W = np.eye(3) #identity matrix 

W0 #optimal solution with identity matrix 

WW = itpr(b,a,0.0001, 5)
WW #optimal solution with iterated weighted matrices with chosen error 0.0001 and 5 iterations. 



