from numpy import matrix, linalg, random
from time import time
def handle(n):
    # LINPACK benchmarks
    int_n = int(n)
    ops = (2.0 * int_n) * int_n * int_n / 3.0 + (2.0 * int_n) * int_n
    # Create AxA array of random numbers -0.5 to 0.5
    A = random.random_sample((int_n, int_n)) - 0.5
    B = A.sum(axis=1)
    # Convert to matrices
    A = matrix(A)
    B = matrix(B.reshape((int_n, 1)))
    # Ax = B
    start = time()
    x = linalg.solve(A, B)
    latency = time() - start
    mflops = (ops * 1e-6 / latency)
    result = {
        'mflops': mflops,
        'latency': latency
    }
    return mflops
