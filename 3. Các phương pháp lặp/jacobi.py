import numpy as np

def jacobi_iterative(n: int, A: np.ndarray, b: np.ndarray, XO: np.ndarray, TOL: float, N: int):
    '''
    INPUT the number of equations and unknowns n; the entries ai j , 1 ≤ i, j ≤ n of the matrix A; the entries bi , 1 ≤ i ≤ n of b; the entries XOi , 1 ≤ i ≤ n of XO = x(0) ; tolerance TOL; maximum number of iterations N.
    OUTPUT the approximate solution x1 , . . . , xn or a message that the number of iterations was exceeded.
    '''
    print("\nStart iterating...")
    x = np.zeros(n, np.float64)
    k = 1
    try:
        while k <= N:
            for i in range(n):
                x[i] = 1/A[i][i] * (-np.sum([A[i][j] * XO[j] for j in range(n) if j != i]) + b[i])
            print(f"x^({k}) = {x}")
            if np.linalg.norm(x - XO) < TOL:
                print(f"\nThe result is {x}")
                return
            k += 1
            for i in range(n):
                XO[i] = x[i]
        print(f'\nMethod failed after {N} iterations') 
    except OverflowError:
        print(f'\nMethod diverged after {i-1} iterations')
    print('The procedure was unsuccessful.') 
    
if __name__ == '__main__':
    print("To solve Ax = b given an initial approximation x^(0)")
    A = np.array([
        [10, -1, 2, 0],
        [-1, 11, -1, 3],
        [2, -1, 10, -1],
        [0, 3, -1, 8]
    ], np.float64)
    b = np.array([6, 25, -11, 15], np.float64)
    XO = np.array([0, 0, 0, 0], np.float64)
    TOL = 1e-3 # equal 0.001 or 10^-3
    N = 20
    print(f"Inital approx: {XO}")

    jacobi_iterative(len(A), A, b, XO, TOL, N)