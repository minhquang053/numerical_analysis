import numpy as np


def solve(initial_value, a, b, N, f):
    h = (b - a) / N
    result = np.zeros(shape=(N + 1,))
    result[0] = initial_value
    # print(result)
    for i in range(1, N + 1):
        result[i] = result[i - 1] + h * f(a + (i - 1) * h, result[i - 1])
    return result


initial_value = [1, -1 / np.log(2), -2, 1]
a = [0, 1, 1, 0]
b = [1, 2, 3, 1]
N = [10, 10, 10, 10]
f = [
    lambda t, y: (2 - 2 * t * y) / (t**2 + 1),
    lambda t, y: y**2 / (1 + t),
    lambda t, y: (y**2 + y) / t,
    lambda t, y: -t * y + 4 * t / y,
]
P = [
    lambda t: (2 * t + 1) / (t**2 + 1),
    lambda t: -1 / np.log(t + 1),
    lambda t: 2 * t / (1 - 2 * t),
    lambda t: np.sqrt(4 - 3 * np.exp(-(t**2))),
]

problems = ["a", "b", "c", "d"]
for i, problem in enumerate(problems):
    print(f"\nSolving problem ({problem})")
    euler_result = solve(initial_value[i], a[i], b[i], N[i], f[i])
    actual_result = P[i](np.linspace(a[i], b[i], N[i] + 1))
    print("Euler result:", euler_result)
    print("Actual result:", actual_result)
    print("Error:", np.abs(euler_result - actual_result))
