from numba import njit, jit

@njit
def loop(trials):
	for i in range(trials):
		i**2
