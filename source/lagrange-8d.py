import numpy as np


def lagrange_polynomial(x) -> float:
    return sum([f_[k] * L(n, k)(x) for k in range(0, n + 1)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n + 1) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n + 1) if i != k]
    )


def f(x) -> float:
    return np.log(np.e**x + 2)


x_ = np.array([-1, -0.5, 0, 0.5], np.float64)
f_ = np.array([0.86199480, 0.95802009, 1.0986123, 1.2943767], np.float64)
x_to_approx = 0.25

n = 1
print(f"Lagrange polynomial of degree {n}")
print(f"Error bound: 2.74945")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")

n = 2
print(f"\nLagrange polynomial of degree {n}")
print(f"Error bound: 0.357927")
approximation = lagrange_polynomial(x_to_approx)
print(f"Approximation: f({x_to_approx}) = {approximation}")
print(f"=> Actual error = {abs(f(x_to_approx) - approximation)}")
