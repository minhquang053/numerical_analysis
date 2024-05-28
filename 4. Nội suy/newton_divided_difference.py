import numpy as np
from utils import plot_points_and_points


def newton_divided_difference(x_: list[float], f_: list[list[float]]) -> float:
    F_ = np.zeros((n + 1, n + 1), np.float64)
    for i in range(n + 1):
        F_[i][0] = f_[i]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            F_[i][j] = (F_[i][j - 1] - F_[i - 1][j - 1]) / (x_[i] - x_[i - j])

    res = [F_[i][i] for i in range(n + 1)]
    print(res)
    return res


def P(x):
    return F[0] + np.sum(
        [F[i] * np.prod([x - x_[j] for j in range(i)]) for i in range(1, n + 1)]
    )


x_ = np.array([1.0, 1.3, 1.6, 1.9, 2.2], np.float64)
f_ = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623], np.float64)

assert len(x_) == len(f_), "data length not match"
n = len(x_) - 1
F = newton_divided_difference(x_, f_)

print("Estimated with Newton Divided Difference Formula")
x_to_approx = [1.0, 1.5, 2.0, 2.5, 3.0]
estimated_points = [(x, P(x)) for x in x_to_approx]

for point in estimated_points:
    print(f"P_{n}({point[0]}) = {point[1]}")

plot_points_and_points(list(zip(x_, f_)), estimated_points)
