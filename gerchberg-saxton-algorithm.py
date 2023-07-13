import numpy as np
from scipy.fftpack import fft, ifft
phi=np.random.random(n)*2*np.pi #generating random phase 
y_o=np.abs(x)*np.exp(1j*phi) #this starts the initialization of the code 
F_1=fft(y_o) #this starts the general step
y_1p=ifft(np.abs(F)*F_1/np.abs(F_1))
y_1=np.abs(x)*y_1p/np.abs(y_1p)
F = fft(x)
MX=np.abs(x)
MF=np.abs(fft(x))

def find_next(y,MX,MF) : 
    Fy=fft(y)
    yp=ifft(MF*Fy/np.abs(Fy))
    #print(Fy,yp)
    return MX*yp/np.abs(yp)
    
y_o = MX*np.exp(1j*phi)

#Now this is the iterative step of the GS algorithm, where n is the length of the input vector (which can be changed depending on the desired input)
n = 20
x = 2*np.random.random(n)
phi = np.random.random(n)*2*np.pi
MX=np.abs(x)
MF=np.abs(fft(x))
y_o= MX*np.exp(1j*phi)
y_n=y_o
for i in range(50): 
    y_next=find_next(y_n, MX, MF)
    print(np.linalg.norm(y_next-y_n),np.linalg.norm(np.abs(fft(y_n))-MF))
    y_n = y_next
print(y_next,x) 
