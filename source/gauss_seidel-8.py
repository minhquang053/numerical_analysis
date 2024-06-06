import numpy as np
import copy


def gauss_seidel_iterative(
    n: int, A: np.ndarray, b: np.ndarray, XO: np.ndarray, TOL: float, N: int
):
    """
    INPUT the number of equations and unknowns n; the entries ai j , 1 ≤ i, j ≤ n of the matrix A; the entries bi , 1 ≤ i ≤ n of b; the entries XOi , 1 ≤ i ≤ n of XO = x(0) ; tolerance TOL; maximum number of iterations N.
    OUTPUT the approximate solution x1 , . . . , xn or a message that the number of iterations was exceeded.
    """
    print("\nStart iterating...")
    x = np.zeros(n, np.float64)
    k = 1
    x_5 = np.zeros(n, np.float64)
    try:
        while k <= N:
            for i in range(n):
                x[i] = (
                    1
                    / A[i][i]
                    * (
                        -np.sum([A[i][j] * x[j] for j in range(i)])
                        - np.sum([A[i][j] * XO[j] for j in range(i + 1, n)])
                        + b[i]
                    )
                )
            if k == 5:
                x_5 = copy.deepcopy(x)
            print(f"x_({k}) = {x}")
            if np.linalg.norm(x - XO) < TOL:
                print(f"\nAfter 5 iterations, x = {x_5}\n...")
                print(f"After {k} iterations, x = {x}")
                return
            k += 1
            for i in range(n):
                XO[i] = x[i]
        print(f"\nMethod failed after {N} iterations")
    except OverflowError:
        print(f"\nMethod diverged after {i-1} iterations")
    print("The procedure was unsuccessful.")


if __name__ == "__main__":
    print("To solve Ax = b given an initial approximation x^(0)")
    A = np.array([[3, 2, 1], [1, 3, 2], [2, 1, 3]], np.float64)
    b = np.array([7, 4, 7], np.float64)
    XO = np.array([1, 1, 1], np.float64)
    TOL = 1e-10  # equal 0.001 or 10^-3
    N = 100
    print(f"Inital approx: {XO}")

    gauss_seidel_iterative(len(A), A, b, XO, TOL, N)
