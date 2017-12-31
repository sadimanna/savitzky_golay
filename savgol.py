import numpy as np
import time
def savgol1Dcoeff(order=2,nump=5):
	#variable	
	z = np.arange(-(nump-1)/2,(nump+1)/2).reshape(-1,1)
	#Jacobian
	J = np.hstack(np.power(z,n) for n in xrange(order+1))
	JT = np.transpose(J)
	JTJ = np.matmul(JT,J)
	iJTJ = np.linalg.inv(JTJ)
	C = np.matmul(iJTJ,JT) #iJTJ_JT
	return C

def savgolfilt(data,order=2,nump=5,h=2):
	savgolcoeff = savgol1Dcoeff(order,nump)
	#Since we need only the coeff a0
	coeff = savgolcoeff[0,:]
	print coeff
	#padding the original data for taking the boundary values
	pad_length = h*(nump-1)/2
	half_window = pad_length
	data_pad  = np.pad(data,(pad_length,pad_length),'constant',constant_values=(0,0))
	data_len = len(data)
	data_pad_len = len(data_pad)
	new_data = np.zeros(data_len)
	for i in xrange(pad_length,data_pad_len-pad_length):
		data_window = data_pad[i-half_window:i+half_window+1]
		data_smooth = data_window[[h*n for n in xrange(nump)]]
		new_data[i-pad_length] = np.sum(np.multiply(data_smooth,coeff))
	return new_data

'''stime = time.time()
#print savgol1Dcoeff(3,5)
#print savgol1Dcoeff(3,7)
#print savgol1Dcoeff(3,9)
#print savgol1Dcoeff(3,11)
print savgol1Dcoeff(3,13) #this step takes 3.2 milliseconds approx
print time.time()-stime
import matplotlib.pyplot as plt
s = np.random.random(100)*5 - 2.5
plt.plot(s,'b')
snew = savgolfilt(s,2,7,1)
snew2 = savgolfilt(s,2,5,1)
snew3 = savgolfilt(s,2,11,1)
plt.plot(snew,'r')
plt.plot(snew2,'g')
plt.plot(snew3,'y')
plt.show()'''
