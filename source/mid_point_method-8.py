import numpy as np

np.set_printoptions(10)


def f(x, y):
    pass


# Input
# initial_value: y(a)
# a, b: boundaries
# N: intervals
# f: differential function
# s: actual solution
def solve(initial_value, a, b, N, f, s):
    approximation = np.zeros(shape=(N + 1,))
    actual_result = np.zeros(shape=(N + 1,))
    h = (b - a) / N
    for i in range(N + 1):
        if i == 0:
            approximation[i] = initial_value
            actual_result[i] = initial_value
        else:
            temp = approximation[i - 1] + h / 2 * f(
                a + (i - 1) * h, approximation[i - 1]
            )
            approximation[i] = approximation[i - 1] + h * f(a + (i - 1 / 2) * h, temp)
            actual_result[i] = s(a + i * h)
    print("Approximation:", approximation)
    print("Actual result:", actual_result)
    print("Errors:", np.abs(approximation - actual_result))
    print("MSE:", np.sum((approximation - actual_result) ** 2) / (N + 1))


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
s = [
    lambda t: (2 * t + 1) / (t**2 + 1),
    lambda t: -1 / np.log(t + 1),
    lambda t: 2 * t / (1 - 2 * t),
    lambda t: np.sqrt(4 - 3 * np.exp(-(t**2))),
]

problems = ["a", "b", "c", "d"]
for i, problem in enumerate(problems):
    print(f"\nSolution for problem ({problem}):")
    solve(initial_value[i], a[i], b[i], N[i], f[i], s[i])
