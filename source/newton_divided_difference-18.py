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


def newton_divided_difference(x_: list[float], f_: list[list[float]]) -> float:
    F_ = np.zeros((n + 1, n + 1), np.float64)
    for i in range(n + 1):
        F_[i][0] = f_[i]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            F_[i][j] = (F_[i][j - 1] - F_[i - 1][j - 1]) / (x_[i] - x_[i - j])

    res = [F_[i][i] for i in range(n + 1)]
    print(f"The i-th divided difference is consecutively:\n{res}")
    return res


def P(x):
    return F[0] + np.sum(
        [F[i] * np.prod([x - x_[j] for j in range(i)]) for i in range(1, n + 1)]
    )


x_ = np.array([1950, 1960, 1970, 1980, 1990, 2000], np.float64)
f_ = np.array([151326, 179323, 203302, 226542, 249633, 281422], np.float64)

assert len(x_) == len(f_), "data length not match"
n = len(x_) - 1
F = newton_divided_difference(x_, f_)

print("\nRandom points estimated with Newton Divided Difference Formula")
x_to_approx = [1940, 1950, 1955, 1965, 1975, 1985, 1995, 2000, 2005, 2010, 2015, 2020]
estimated_points = [(x, P(x)) for x in x_to_approx]

for point in estimated_points:
    print(f"P_{n}({point[0]}) = {point[1]}")

print("\nResult for approximating population of the US:")
for point in estimated_points:
    if point[0] in [1940, 1975, 2020]:
        print(f"There will be {int(point[1]) * 1000:,} people in {point[0]}")

print("\nThe reported population of the US in 1975 is 216 million people")
print("==> Good approximation")
print("The reported population of the US in 2020 is 329,5 million people")
print("==> Bad approximation")

plot_points_and_points(list(zip(x_, f_)), estimated_points)
