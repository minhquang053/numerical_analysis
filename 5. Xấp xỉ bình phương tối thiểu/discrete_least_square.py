import numpy as np


def linear_least_squares():
    a = [
        [np.sum([x_[i] ** j for i in range(m)]) for j in range(k, k + n + 1)]
        for k in range(n + 1)
    ]
    b = [np.sum([y_[i] * x_[i] ** j for i in range(m)]) for j in range(n + 1)]
    print(f"a = {a}")
    print(f"b = {b}")
    return a, b


def P(x):
    return np.sum([res[i] * (x**i) for i in range(n + 1)])


if __name__ == "__main__":
    x_ = np.array([0, 0.25, 0.50, 0.75, 1.00], np.float64)
    y_ = np.array([1.0000, 1.2840, 1.6487, 2.1170, 2.7183], np.float64)
    n = 2
    m = len(x_)
    a, b = linear_least_squares()
    res = np.linalg.solve(a, b)
    print(f"x = {res}")

    x_to_approx = [i * 0.1 for i in range(10)]
    estimated_points = [(x, P(x)) for x in x_to_approx]

    print("\nEstimated with Linear Least Squares Polynomial")
    for point in estimated_points:
        print(point)

    plot_points_and_points(
        list(zip(x_, y_)),
        estimated_points,
    )
