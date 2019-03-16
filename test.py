import numpy as np
from numba import njit, jit
from datetime import datetime

@jit
def loop1(trials):
	for i in np.linspace(start=1,stop=trials,num=trials):
		i*i

def loop2(trials):
	for i in range(trials):
		i*i

start_time1 = datetime.now()
loop1(1000000)
end_time1 = datetime.now()

start_time2 = datetime.now()
loop2(1000000)
end_time2 = datetime.now()

print('Execusion time Numba: ', end_time1 - start_time1)
print('Execusion time Normal: ', end_time2 - start_time2)