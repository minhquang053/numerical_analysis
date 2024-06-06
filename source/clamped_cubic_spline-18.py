import numpy as np
from autograd import grad
from scipy import integrate


def clamped_cubic_spline():
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

    alpha[0] = 3 * (a[1] - a[0]) / h[0] - 3 * FPO
    alpha[n] = 3 * FPN - 3 * (a[n] - a[n - 1]) / h[n - 1]

    for i in range(1, n):
        alpha[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]

    l[0] = 2 * h[0]
    u[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n):
        l[i] = 2 * (x_[i + 1] - x_[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = h[n - 1] * (2 - u[n - 1])
    z[n] = (alpha[n] - h[n - 1] * z[n - 1]) / l[n]
    c[n] = z[n]

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    res = [(a[j], b[j], c[j], d[j]) for j in range(n)]
    print("The cubic polynomials is calculated with:")
    for i, cubic_polynomial in enumerate(res):
        print(f"(a_{i}, b_{i}, c_{i}, d_{i}) = {cubic_polynomial}")
    return res


def S(x):
    if x < x_[0]:
        piece = pieces[0]
        return (
            piece[0]
            + piece[1] * (x - x_[0])
            + piece[2] * (x - x_[0]) ** 2
            + piece[3] * (x - x_[0]) ** 3
        )
    elif x > x_[-1]:
        piece = pieces[-1]
        return (
            piece[0]
            + piece[1] * (x - x_[-1])
            + piece[2] * (x - x_[-1]) ** 2
            + piece[3] * (x - x_[-1]) ** 3
        )
    for i, piece in enumerate(pieces):
        if x >= x_[i] and x <= x_[i + 1]:
            return (
                piece[0]
                + piece[1] * (x - x_[i])
                + piece[2] * (x - x_[i]) ** 2
                + piece[3] * (x - x_[i]) ** 3
            )


def f(x):
    return np.e ** (-x)


def grad_f(x):
    return -np.e ** (-x)


def second_grad_f(x):
    return f(x)


x_ = np.array([0, 0.25, 0.75, 1.0], np.float64)
f_ = np.array([f(x) for x in x_], np.float64)

# two endpoints
FPO = -1
FPN = -np.e ** (-1)

# or we can calculate using autograd
# FPO = grad(f)(0)
# FPN = grad(f)(3)


n = len(x_) - 1
pieces = clamped_cubic_spline()

print(f"\nIntegration of actual function in [0, 1]: {integrate.quad(f, 0, 1)[0]}")
print(f"Integration of the cubic spline in [0, 1]: {integrate.quad(S, 0, 1)[0]}")
print("==> Very close")

print(f"\nActual value of f'(0.5) = {grad_f(0.5)}")
print(f"Approximation of f'(0.5): {grad(S)(0.5)}")
print("==> Very close")

print(f"\nActual value of f''(0.5) = {second_grad_f(0.5)}")
print(f"Approximation of f''(0.5): {grad(grad(S))(0.5)}")
print("==> Pretty close")
