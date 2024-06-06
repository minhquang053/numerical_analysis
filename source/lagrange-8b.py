import numpy as np


def lagrange_polynomial(x) -> float:
    return sum([f_[k] * L(n, k)(x) for k in range(0, n + 1)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n + 1) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n + 1) if i != k]
    )


def f(x) -> float:
    return x**4 - x**3 + x**2 - x + 1


x_ = np.array([-0.5, -0.25, 0.25, 0.5], np.float64)
f_ = np.array([1.93750, 1.33203, 0.800781, 0.687500], np.float64)
x_to_approx = 0

n = 1
print(f"Lagrange polynomial of degree {n}")
print(f"Error bound: 0.5")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")

n = 2
print(f"\nLagrange polynomial of degree {n}")
print(f"Error bound: 0.09903")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")
