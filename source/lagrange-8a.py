import numpy as np


def lagrange_polynomial(x) -> float:
    return sum([f_[k] * L(n, k)(x) for k in range(0, n + 1)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n + 1) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n + 1) if i != k]
    )


def f(x) -> float:
    return np.e ** (2 * x)


x_ = np.array([0, 0.25, 0.5, 0.75], np.float64)
f_ = np.array([1, 1.64872, 2.71828, 4.48169], np.float64)
x_to_approx = 0.43

n = 1
print(f"Lagrange polynomial of degree {n}")
print(f"Error bound: 0.67957")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")

n = 2
print(f"\nLagrange polynomial of degree {n}")
print(f"Error bound: 0.02178")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")
