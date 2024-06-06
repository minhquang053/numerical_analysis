import numpy as np

np.set_printoptions(10)


def second_order_differential(Z):
    # Problem a
    return np.array([Z[1], -32.17 / 2 * np.sin(Z[0])])


def solve(initial_values, a, b, N):
    h = (b - a) / N
    result = np.zeros(shape=(N + 1,))
    result[0] = initial_values[0]
    Z = initial_values
    for i in range(N):
        Z_diff = second_order_differential(Z)
        Z += h * Z_diff
        result[i + 1] = Z[0]
    return result


print(solve(np.array([np.pi / 6, 0], dtype=np.float64), 0, 2, 20))
