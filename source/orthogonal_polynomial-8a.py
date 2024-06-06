import numpy as np
from scipy import integrate
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


def orthogonal_polynomials() -> list[callable]:
    return [
        lambda x: 1,
        lambda x: x - 1 / 2,
        lambda x: x**2 - x + 1 / 6,
        lambda x: x**3 - (3 / 2) * x**2 + (3 / 5) * x - 1 / 20,
    ]


def orthogonal_polynomials_repr() -> list[str]:
    return ["1", "x - 1/2", "x^2 - x + 1/6", "x^3 - (3/2)x^2 + (3/5)x - 1/20"]


def P(x):
    return np.sum(
        [
            integrate.quad(lambda x: op[j](x) * f(x), a, b)[0]
            / integrate.quad(lambda x: op[j](x) ** 2, a, b)[0]
            * op[j](x)
            for j in range(n + 1)
        ]
    )


def f(x):
    return x**2 + 3 * x + 2


if __name__ == "__main__":
    op: list[callable] = orthogonal_polynomials()
    opr: list[str] = orthogonal_polynomials_repr()
    a, b = (0, 1)
    n = 1
    pieces = [
        f"{integrate.quad(lambda x: op[j](x) * f(x), a, b)[0] / integrate.quad(lambda x: op[j](x) ** 2, a, b)[0]}({opr[j]})"
        for j in range(n + 1)
    ]
    print(f"f(x) = {' + '.join(pieces)}")
    x_to_approx = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    P_approx = [P(x) for x in x_to_approx]
    f_approx = [f(x) for x in x_to_approx]
    plot_points_and_points(
        list(zip(x_to_approx, f_approx)), list(zip(x_to_approx, P_approx))
    )
