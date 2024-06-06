import numpy as np


def gauss_elimination_backward_substitution(n: int, A: np.ndarray):
    """
    INPUT number of unknowns and equations n; augmented matrix A = [ai j ], where 1 ≤ i ≤ n and 1 ≤ j ≤ n + 1.
    OUTPUT solution x1, x2 ,..., xn or message that the linear system has no unique solution.
    """
    print("\nSolving...")
    x = np.zeros(n + 1)
    for i in range(n):
        for p in range(i, n + 1):
            if A[p][i] != 0:
                if p != i:
                    A[[i, p]] = A[[p, i]]
                break
        else:
            print("No unique solution exists")
            return
        for j in range(i + 1, n + 1):
            if A[i][i] != 0 and not np.isnan(A[i][i]):
                factor = A[j][i] / A[i][i]
                A[j] = A[j] - factor * A[i]
    print(f"Row echelon form:\n{A}")
    if A[n][n] == 0:
        print("No unique solution exists")
        return
    x[n] = A[n][n + 1] / A[n][n]
    for i in range(n - 1, -1, -1):
        if A[i][i] != 0 and not np.isnan(A[i][i]):
            x[i] = (
                A[i][n + 1] - np.sum([A[i][j] * x[j] for j in range(i + 1, n + 1)])
            ) / A[i][i]
    print(f"\nThe result is x = {x}\nProcedure completed successfully")


if __name__ == "__main__":
    print(
        "Gause Elimination with Backward Substitution: To solve the n × n linear system"
    )
    # Chú ý: vẫn phải thêm dòng [0 .. 0] vào phía dưới nếu không đủ n phương trình
    E = np.array(
        [
            [1, 1, -1, 1, -1, 2],
            [2, 2, 1, -1, 1, 4],
            [3, 1, -3, -2, 3, 8],
            [4, 1, -1, 4, -5, 16],
            [16, -1, 1, -1, -1, 32],
        ],
        np.float64,
    )
    print(f"Augmented matrix:\n{E}")
    gauss_elimination_backward_substitution(len(E) - 1, E)
