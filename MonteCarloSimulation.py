import numpy as np
import matplotlib.pyplot as plt
import math

def montecarlosimulation (needles_dropped,trials):
	'''
	input the number of needles to drop and the number
	of trails to run
	'''
	pi = list()
	for trial in range(1,trials):
		in_circle = 0
		for pair in np.random.rand(needles_dropped,2)**2:
			if pair[0] + pair[1] < 1:
				in_circle += 1
		pi.append(in_circle/needles_dropped*4)
	return pi

diff = 100
num_needles = 10
while diff > 0.0001:
	pi_estimates = montecarlosimulation(needles_dropped=num_needles,trials=10000)
	diff = abs(math.pi - np.mean(pi_estimates))
	print('mean: ',np.mean(pi_estimates),',',
		  'std: ',np.std(pi_estimates),',',
		  'number of needles used: ',num_needles)
	num_needles += 5

plt.hist(pi_estimates,bins=100)
plt.show()