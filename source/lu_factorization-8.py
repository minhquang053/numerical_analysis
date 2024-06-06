import numpy as np


def cholesky_lu_factorization(n: int, A: np.ndarray) -> np.ndarray:
    print("\nSolving...")
    l = np.zeros((n, n), np.float64)
    l[0][0] = np.sqrt(A[0][0])
    print(f"l_11 = {l[0][0]}")
    for j in range(1, n):
        l[j][0] = A[j][0] / l[0][0]
        print(f"l_{j+1}1 = {l[j][0]}")

    for j in range(1, n):
        l[j][j] = np.sqrt(A[j][j] - np.sum([(l[j][s]) ** 2 for s in range(j)]))
        print(f"l_{j+1}{j+1} = {l[j][j]}")

        for p in range(j + 1, n):
            l[p][j] = (
                1 / l[j][j] * (A[p][j] - np.sum([l[j][s] * l[p][s] for s in range(j)]))
            )
            print(f"l_{p+1}{j+1} = {l[p][j]}")

    return l


if __name__ == "__main__":
    # Chú ý: vẫn phải thêm dòng [0 .. 0] vào phía dưới nếu không đủ n phương trình
    A = np.array(
        [
            [4, 6, 8],
            [6, 34, 52],
            [8, 52, 129],
        ],
        np.float64,
    )
    b = np.array([0, -160, -452], np.float64)
    L = cholesky_lu_factorization(len(A), A)
    print(f"\nFactorization: L = U =\n{L}")

    y = np.linalg.solve(L, b)
    print(f"\nL . y = b\n==> y = {y}")

    x = np.linalg.solve(L.T, y)
    print(f"\nL_tranpose . x = y\n==> x = {x}")

    print(f"\nThe result for A.x = b is x = {x}")
