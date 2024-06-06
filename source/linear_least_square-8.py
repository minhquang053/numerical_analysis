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
        x1, y1 = zip(*points_1)
        plt.scatter(x1, y1, color="blue", label="Data points")

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


def linear_least_square():
    upper_0 = np.sum([x_[i] ** 2 for i in range(m)]) * np.sum(
        [y_[i] for i in range(m)]
    ) - np.sum([x_[i] * y_[i] for i in range(m)]) * np.sum([x_[i] for i in range(m)])
    lower_0 = m * (np.sum([x_[i] ** 2 for i in range(m)])) - (
        np.sum([x_[i] for i in range(m)]) ** 2
    )
    a_0 = upper_0 / lower_0
    upper_1 = m * np.sum([x_[i] * y_[i] for i in range(m)]) - np.sum(
        [x_[i] for i in range(m)]
    ) * np.sum([y_[i] for i in range(m)])
    lower_1 = (
        m * np.sum([x_[i] ** 2 for i in range(m)])
        - np.sum([x_[i] for i in range(m)]) ** 2
    )
    a_1 = upper_1 / lower_1
    print(f"a_0 = {a_0}")
    print(f"a_1 = {a_1}")
    return a_0, a_1


def P(x):
    return a_0 + a_1 * x


def root_of_line(y):
    return (y - a_0) / a_1


if __name__ == "__main__":
    x_ = np.array(
        [
            302,
            325,
            285,
            339,
            334,
            322,
            331,
            279,
            316,
            347,
            343,
            290,
            326,
            233,
            254,
            323,
            337,
            337,
            304,
            319,
            234,
            337,
            351,
            339,
            343,
            314,
            344,
            185,
            340,
            316,
        ],
        np.float64,
    )
    y_ = np.array(
        [
            45,
            72,
            54,
            54,
            79,
            65,
            99,
            63,
            65,
            99,
            83,
            74,
            76,
            57,
            45,
            83,
            99,
            70,
            62,
            66,
            51,
            53,
            100,
            67,
            83,
            42,
            79,
            59,
            75,
            45,
        ],
        np.float64,
    )
    m = len(x_)
    a_0, a_1 = linear_least_square()
    print(f"\nThe linear least square polynomial is:\ny = {a_0} + {a_1}x")

    print(f"\nTo secure 90%, we have to do about {root_of_line(90)} homeworks")
    print(f"To secure 60%, we have to do about {root_of_line(60)} homeworks")

    x_to_approx = [i for i in range(180, 400, 10)]
    estimated_points = [(x, P(x)) for x in x_to_approx]

    plot_points_and_points(
        list(zip(x_, y_)),
        estimated_points,
    )
