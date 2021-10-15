import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as m
def vec(x,y):
	return np.array([x,y])

def plo(x,y):
	return [np.array((x[0],y[0])),np.array((x[1],y[1]))]


R_90 = np.array([[0,-1],[1,0]])

R_270 = np.array([[0,1],[-1,0]])
p = vec(0,0)

T = ["T_1","T_2","T_3"]

def fractal(x,n,T):
	
	while n > 0:
		Tr = rand.choice(T)


		if Tr == "T_1":
			x = abs(0.5*x)
			plt.scatter(*x,s=5)
			n = n - 1
			
		elif Tr == "T_2":
			x = 0.5*x
			
			x = np.dot(R_270,x)
			x =abs( vec(x[0],x[1]+1))
			plt.scatter(*x,s=5)
			n = n - 1
			
		else:
			x = 0.5*x
			
			x = np.dot(R_90,x)
			x = abs(vec(x[0]+1,x[1]))

			plt.scatter(*x,s=5)
			n = n - 1
			



if __name__ == '__main__':
	n =10000
	plt.scatter(*p,s=5)
	
	fractal(p,n,T)




	plt.show()
