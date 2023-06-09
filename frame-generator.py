import numpy as np
n=3 #n is the dimension of the space
m=9 #m is the number of frame elements you want

#Creating random frames of unit vector
X=np.random.rand(m,n)
print(X)

for k in range(1,m+1):
    k=k/np.sqrt(np.sum(X**2))
    print(k)
    
#Reconstruction of arbitrary vector 
x = np.random.rand(n,1)
x=x/np.sqrt(np.sum(x)**2)
norm_x = np.sqrt(x**2)

#Calculate frame coefficients
X_fc= np.matmul(np.transpose(X), x)
X_fc
