import numpy as np


def three_point_end_point(x_0: float, last_point=False) -> None:
    idx = np.where(x_ == x_0)[0][0]
    if last_point:
        res = 1 / (2 * -h) * (-3 * f_[idx] + 4 * f_[idx - 1] - f_[idx - 2])
    else:
        res = 1 / (2 * h) * (-3 * f_[idx] + 4 * f_[idx + 1] - f_[idx + 2])
    print(f"3-Point Endpoint Formula: f'({x_0}) = {res}")
    return res


def three_point_mid_point(x_0: float) -> None:
    idx = np.where(x_ == x_0)[0][0]
    res = 1 / (2 * h) * (f_[idx + 1] - f_[idx - 1])
    print(f"3-Point Midpoint Formula: f'({x_0}) = {res}")
    return res


def five_point_end_point(x_0: float, last_point=False) -> None:
    idx = np.where(x_ == x_0)[0][0]
    if last_point:
        res = (
            1
            / (12 * -h)
            * (
                -25 * f_[idx]
                + 48 * f_[idx - 1]
                - 36 * f_[idx - 2]
                + 16 * f_[idx - 3]
                - 3 * f_[idx - 4]
            )
        )
    else:
        res = (
            1
            / (12 * h)
            * (
                -25 * f_[idx]
                + 48 * f_[idx + 1]
                - 36 * f_[idx + 2]
                + 16 * f_[idx + 3]
                - 3 * f_[idx + 4]
            )
        )
    print(f"5-Point Endpoint Formula: f'({x_0}) = {res}")


def five_point_mid_point(x_0: float) -> None:
    idx = np.where(x_ == x_0)[0][0]
    res = 1 / (12 * h) * (f_[idx - 2] - 8 * f_[idx - 1] + 8 * f_[idx + 1] - f_[idx + 2])
    print(f"5-Point Midpoint Formula: f'({x_0}) = {res}")


def second_derivative_midpoint_formula(x_0: float) -> float:
    idx = np.where(x_ == x_0)[0][0]
    res = 1 / (h**2) * (f_[idx - 1] - 2 * f_[idx] + f_[idx + 1] - f_[idx + 2])
    print(f"2nd Derivative Midpoint Formula: f''({x_0}) = {res}")


def f(x: float) -> float:
    return (np.cos(3 * x)) ** 2 - np.e ** (2 * x)


def grad_f(x: float) -> float:
    return -6 * np.cos(3 * x) * np.sin(3 * x) - 2 * np.e ** (2 * x)


if __name__ == "__main__":
    x_ = np.array([0.2, 0.4, 0.6, 0.8, 1.0], np.float64)
    f_ = np.array([0.9798652, 0.9177710, 0.808038, 0.6386093, 0.3843735], np.float64)
    h = x_[1] - x_[0]
    print("(a)")
    three_point_mid_point(0.4)
    second_derivative_midpoint_formula(0.4)
    print("\n(b)")
    five_point_mid_point(0.6)
    second_derivative_midpoint_formula(0.6)
