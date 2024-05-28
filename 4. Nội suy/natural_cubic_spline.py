import numpy as np
from utils import plot_points_and_func


def natural_cubic_spline():
    a = [f_[i] for i in range(n + 1)]
    b = [0.0 for _ in range(n + 1)]
    c = [0.0 for _ in range(n + 1)]
    d = [0.0 for _ in range(n + 1)]
    h = [0.0 for _ in range(n + 1)]
    alpha = [0.0 for _ in range(n + 1)]
    l = [0.0 for _ in range(n + 1)]
    u = [0.0 for _ in range(n + 1)]
    z = [0.0 for _ in range(n + 1)]

    for i in range(n):
        h[i] = x_[i + 1] - x_[i]

    for i in range(1, n):
        alpha[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]

    l[0] = 1

    for i in range(1, n):
        l[i] = 2 * (x_[i + 1] - x_[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c[n] = 0

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    res = [(a[j], b[j], c[j], d[j]) for j in range(n)]
    print(res)
    return res


def S(x):
    for i, piece in enumerate(pieces):
        if x >= x_[i] and x <= x_[i + 1]:
            return (
                piece[0]
                + piece[1] * (x - x_[i])
                + piece[2] * (x - x_[i]) ** 2
                + piece[3] * (x - x_[i]) ** 3
            )


def f(x):
    return np.e**x


x_ = np.array([0, 1, 2, 3], np.float64)
f_ = np.array([1, np.e, np.e**2, np.e**3], np.float64)
n = len(x_) - 1
pieces = natural_cubic_spline()

x_to_approx = [i * 0.2 for i in range(10)]
estimated_points = [(x, S(x)) for x in x_to_approx]

print("Estimated with Natural Cubic Spline")
for point in estimated_points:
    print(point)

plot_points_and_func(estimated_points, f)
