import numpy as np


def lagrange_polynomial(x) -> float:
    return sum([f_[k] * L(n, k)(x) for k in range(0, n + 1)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n + 1) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n + 1) if i != k]
    )


def f(x) -> float:
    return x**2 * np.cos(x) - 3 * x


x_ = np.array([0.1, 0.2, 0.3, 0.4], np.float64)
f_ = np.array([-0.29004986, -0.56079734, -0.81401972, -1.0526302], np.float64)
x_to_approx = 0.18

n = 1
print(f"Lagrange polynomial of degree {n}")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")

n = 2
print(f"\nLagrange polynomial of degree {n}")
print(f"Error bound: 0.0002235")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")
