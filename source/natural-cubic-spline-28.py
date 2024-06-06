import numpy as np
import matplotlib.pyplot as plt


def plot_points_and_points(points_1=None, points_2=None):
    """
    Plot points and/or a given function over the x-axis range determined by the points.

    Parameters:
    points (list of tuples): List of (x, y) points to be plotted.
    func (function): The function to plot.
    """
    plt.figure(figsize=(8, 6))

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


x_ = np.array([1950, 1960, 1970, 1980, 1990, 2000], np.float64)
f_ = np.array([151326, 179323, 203302, 226542, 249633, 281422], np.float64)
n = len(x_) - 1
pieces = natural_cubic_spline()

x_to_approx = [1940, 1950, 1955, 1965, 1975, 1985, 1995, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020]
estimated_points = [(x, S(x)) for x in x_to_approx]

print("\nRandom points estimated with Natural Cubic Spline")
for point in estimated_points:
    print(point)

print("\nResult for approximating population of the US:")
for point in estimated_points:
    if point[0] in [1940, 1975, 2020]:
        print(f"There will be {int(point[1]) * 1000:,} people in {point[0]}")

print("\nThe reported population of the US in 1975 is 216 million people")
print("==> Good approximation")
print("The reported population of the US in 2020 is 329,5 million people")
print("==> Good approximation")

plot_points_and_points(list(zip(x_, f_)), estimated_points)
