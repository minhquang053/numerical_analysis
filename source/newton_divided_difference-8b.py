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


x_ = np.array([0.0, 0.1, 0.3, 0.6, 1.0, 1.1], np.float64)
f_ = np.array([-6.0, -5.89483, -5.65014, -5.17788, -4.28172, -3.99583], np.float64)

assert len(x_) == len(f_), "data length not match"
n = 5
F = newton_divided_difference(x_, f_)

print("\nRandom points estimated with Newton Divided Difference Formula")
x_to_approx = [0.0, 0.2, 0.4, 0.5, 0.7, 0.9, 1.1]
estimated_points = [(x, P(x)) for x in x_to_approx]

for point in estimated_points:
    print(f"P_{n}({point[0]}) = {point[1]}")

plot_points_and_points(list(zip(x_, f_)), estimated_points)
