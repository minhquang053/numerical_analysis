import numpy as np
from utils import plot_points_and_func


def lagrange_polynomial(x) -> float:
    n = len(x_)
    return sum([f(x_[k]) * L(n, k)(x) for k in range(0, n)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n) if i != k]
    )


def f(x) -> float:
    return 1 / x


x_ = np.array([2, 2.75, 4], np.float64)
x_to_approx = [i for i in range(1, 6)]
estimated_points = [(x, lagrange_polynomial(x)) for x in x_to_approx]

print("Estimated with Lagrange Polynomial")
for point in estimated_points:
    print(point)

plot_points_and_func(estimated_points, f)
