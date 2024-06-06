import numpy as np


def gauss_jordan_inverse(matrix):
    n = len(matrix)
    aug_matrix = np.hstack([matrix, np.eye(n)])

    for i in range(n):
        pivot_row = max(range(i, n), key=lambda j: abs(aug_matrix[j, i]))
        aug_matrix[[i, pivot_row]] = aug_matrix[[pivot_row, i]]

        pivot_val = aug_matrix[i, i]
        aug_matrix[i] /= pivot_val

        for j in range(n):
            if i != j:
                ratio = aug_matrix[j, i]
                aug_matrix[j] -= ratio * aug_matrix[i]

    return aug_matrix[:, n:]


# Example usage
matrix = np.array(
    [
        [0.01, 0.0, 0.03],
        [0.0, 0.16, 0.08],
        [0.03, 0.08, 0.14],
    ]
)
inverse_matrix = gauss_jordan_inverse(matrix)

print("Original Matrix:")
print(matrix)

print("\nInverse Matrix:")
print(inverse_matrix)
