import numpy as np

def lu_factorization(n: int, A: np.ndarray, L: np.ndarray, U: np.ndarray):
    '''
    INPUT number of unknowns and equations n; augmented matrix A = [ai j ], where 1 ≤ i ≤ n and 1 ≤ j ≤ n + 1.
    OUTPUT solution x1, x2 ,..., xn or message that the linear system has no unique solution.
    '''
    print("\nSolving...")
    
    # print(f"\nThe result is {x}\nProcedure completed successfully")
    
if __name__ == '__main__':
    print("LU Factorization: To factor the n × n matrix A = [ai j ] into the product of the lower-triangular matrix L = [l_ij]\
and the upper-triangular matrix U = [u_ij]; that is, A = LU, where the main diagonal of\
either L or U consists of all ones:")
    # Chú ý: vẫn phải thêm dòng [0 .. 0] vào phía dưới nếu không đủ n phương trình
    E = np.array([
        [1, -1, 2, -1, -8],
        [2, -2, 3, -3, -20],
        [1, 1, 1, 0, -2],
        [1, -1, 4, 3, 4]
    ], np.float64)
    L = np.array([
        [1, -1, 2, -1, -8],
        [2, -2, 3, -3, -20],
        [1, 1, 1, 0, -2],
        [1, -1, 4, 3, 4]
    ], np.float64)
    U = np.array([
        [1, -1, 2, -1, -8],
        [2, -2, 3, -3, -20],
        [1, 1, 1, 0, -2],
        [1, -1, 4, 3, 4]
    ], np.float64)
    print(f"Augmented matrix:\n{E}")