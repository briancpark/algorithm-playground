import time
import matplotlib.pyplot as plt
import numpy as np

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

mem = {}

def fib_memo(n):
	if n <= 1:
		return n
	if n in mem:
		return mem[n]
	mem[n] = fib_memo(n - 1) + fib_memo(n - 2)
	
	return mem[n]
	
def fib_matrix(n):
    A = np.array([[1, 1], [1, 0]])
    return np.linalg.matrix_power(A, n)[0][1]

def fib_test(n):
	start = time.time()
	print(fib(n))
	end = time.time()
	print("Time took to execute naive: " + str(end - start))
	
	start = time.time()
	print(fib_memo(n))
	end = time.time()
	print("Time took to execute memoized: " + str(end - start))

	start = time.time()
	print(fib_matrix(n))
	end = time.time()
	print("Time took to execute with matrices: " + str(end - start))



def fib_benchmark(n):

    naive_times = []
    dynamic_times = []
    matrix_times = []

    for i in range(n):
        print("Computing Fibonnaci of " + str(i))
        start = time.time()
        fib(i)
        print("...")
        end = time.time()
        naive_times.append(end - start)
        
        start = time.time()
        fib_memo(i)
        print("...")
        end = time.time()
        dynamic_times.append(end - start)

        start = time.time()
        fib_matrix(i)
        print("...")
        end = time.time()
        matrix_times.append(end - start)

    plt.plot(naive_times, "r", dynamic_times, "g", matrix_times, "b")
    plt.xlabel('n')
    plt.ylabel('Time it takes to compute')
    plt.savefig('Dynamic vs. Naive Runtime of Fibbonacci.png')
    plt.show()


fib_benchmark(35)
