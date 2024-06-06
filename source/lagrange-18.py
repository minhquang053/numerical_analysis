import numpy as np


def lagrange_polynomial(x) -> float:
    return sum([f_[k] * L(n, k)(x) for k in range(0, n + 1)])


def L(n, k):
    return lambda x: np.prod([x - x_[i] for i in range(n + 1) if i != k]) / np.prod(
        [x_[k] - x_[i] for i in range(n + 1) if i != k]
    )


def f(x) -> float:
    return np.e ** (2 * x)


x_ = np.array([1950, 1960, 1970, 1980, 1990, 2000], np.float64)
f_ = np.array([151326, 179323, 203302, 226542, 249633, 281422], np.float64)
n = len(x_) - 1
x_to_approx = [1940, 1975, 2020]
estimated_points = [(x, lagrange_polynomial(x)) for x in x_to_approx]

print("Result for approximating population of the US:")
for point in estimated_points:
    print(f"There will be {int(point[1]) * 1000:,} people in {point[0]}")

print("\nThe reported population of the US in 1975 is 216 million people")
print("==> Good approximation")
print("The reported population of the US in 2020 is 329,5 million people")
print("==> Bad approximation")
