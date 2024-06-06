import numpy as np
from autograd import grad
import matplotlib.pyplot as plt


def plot_points_and_points(points_1=None, points_2=None):
    """
    Plot points and/or a given function over the x-axis range determined by the points.

    Parameters:
    points (list of tuples): List of (x, y) points to be plotted.
    func (function): The function to plot.
    """
    plt.figure(figsize=(8, 6))

    # Plot points if provided
    if points_1:
        x_values = [point[0] for point in points_1]
        y_values = [point[1] for point in points_1]
        plt.plot(
            x_values, y_values, "b-", label="Data points"
        )  # Use 'b-' for blue line

        # Determine x-axis range based on points
        x_min = min(x_values)
        x_max = max(x_values)
        x_range = (x_min, x_max)

    if points_2:
        x_values = [point[0] for point in points_2]
        y_values = [point[1] for point in points_2]
        plt.plot(
            x_values, y_values, "r-", label="Estimated points"
        )  # Use 'b-' for blue line

        # Determine x-axis range based on points
        x_min = min(x_values)
        x_max = max(x_values)
        x_range = (x_min, x_max)

    # Add title and labels
    plt.title("Plot")
    plt.xlabel("x")
    plt.ylabel("y")

    # Add a legend
    plt.legend()

    # Show grid
    plt.grid(True)

    # Display the plot
    plt.show()


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
    for i, piece in enumerate(pieces):
        if x >= x_[i] and x <= x_[i + 1]:
            return (
                piece[0]
                + piece[1] * (x - x_[i])
                + piece[2] * (x - x_[i]) ** 2
                + piece[3] * (x - x_[i]) ** 3
            )
    else:
        raise Exception(f"x = {x} is out of segment")


x_ = np.array([-1, -0.5, 0, 0.5], np.float64)
f_ = np.array([0.86199480, 0.95802009, 1.0986123, 1.2943767], np.float64)

# two endpoints
FPO = 0.15536240
FPN = 0.45186276

# or we can calculate using autograd
# FPO = grad(f)(0)
# FPN = grad(f)(3)


n = len(x_) - 1
pieces = clamped_cubic_spline()

x_to_approx = [-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5]
estimated_points = [(x, S(x)) for x in x_to_approx]

print("\nRandom points estimated with Clamped Cubic Spline")
for point in estimated_points:
    print(point)

plot_points_and_points(list(zip(x_, f_)), estimated_points)
