import numpy as np


def approximate(a, b, f):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def error_bound(a, b, f_4):
    x = np.linspace(a, b, 1001)
    return np.max((b - a) ** 5 / 2880 * f_4(x))


a = [-0.25, -0.5, 0.75, np.exp(1)]
b = [0.25, 0, 1.3, np.exp(1) + 1]
f = [
    lambda x: np.cos(x) ** 2,
    lambda x: x * np.log(x + 1),
    lambda x: np.sin(x) ** 2 - 2 * x * np.sin(x) + 1,
    lambda x: 1 / (x * np.log(x)),
]
actual_result = [0.4897127693, 0.0525698072, -0.0203767959, 0.2725138805]
f_4 = [
    lambda x: 8 * (np.cos(x) ** 2 - np.sin(x) ** 2),
    lambda x: 2 * (x + 4) / (1 + x) ** 4,
    lambda x: 8 * np.cos(x) - 8 * np.cos(x) ** 2 - 2 * (x - 4 * np.sin(x)) * np.sin(x),
    lambda x: (
        24
        + 60 * np.log(x)
        + 70 * np.log(x) ** 2
        + 50 * np.log(x) ** 3
        + 24 * np.log(x) ** 4
    )
    / (x**5 * np.log(x) ** 5),
]

problems = ["a", "b", "c", "d"]
for i, problem in enumerate(problems):
    print(f"\nSolving problem ({problem})")
    approximation = approximate(a[i], b[i], f[i])
    print("Approximation:", approximation)
    print("Actual result:", actual_result[i])
    print("Error:", np.abs(approximation - actual_result[i]))
print("Simpson's rule error bound:", error_bound(a[i], b[i], f_4[i]))
