import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(10)

def sketch_graph():
    # Define the range for x values with a small step to handle the discontinuities
    x = np.linspace(-10, 10, 1000)

    # Define y values for y = x
    y1 = x

    # Plot y = x
    plt.plot(x, y1, label="y = x", color="blue")

    # Plot y = tan(x) in segments
    for i in range(1, len(x)):
        if (
            np.abs(x[i] - x[i - 1]) < np.pi / 4
        ):  # Use a step smaller than the distance between asymptotes
            x_segment = x[i - 1 : i + 1]
            y_segment = np.tan(x_segment)
            if np.all(
                np.abs(y_segment) < 10
            ):  # Only plot if tan(x) values are within the y limits
                plt.plot(x_segment, y_segment, color="red")

    # Set y limits to avoid large values due to tan(x) asymptotes
    plt.ylim(-10, 10)

    # Add grid, legend, title, and labels
    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title("Graph of y = x and y = tan(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    # Show the plot
    plt.show()


def bisection(a: float, b: float, TOL: float, N_0: int):
    """
    INPUT endpoints a, b; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    """
    assert f(a) * f(b) < 0, f"f({a}) * f({b}) must be negative"
    print("\nStart iterating...")
    i = 1
    FA = f(a)
    while i <= N_0:
        p = a + (b - a) / 2
        print(f"p_{i} = {p}")
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            print(f"\nThe result is x = {p}")
            return
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print(f"\nMethod failed after {N_0} iterations\nThe procedure was unsuccessfull.")


def f(x: float) -> float:
    return x - np.tan(x)


if __name__ == "__main__":
    print(
        "Bisection: To ﬁnd a solution to f (x) = 0 given the continuous function f on the interval [a, b], where f (a) and f (b) have opposite signs:"
    )
    a = 4
    b = 4.6
    tol = 1e-5
    num_iters = 100

    bisection(a, b, tol, num_iters)
    sketch_graph()
