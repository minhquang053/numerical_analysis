import numpy as np
from autograd import grad


def three_point_end_point(x_0: float, last_point=False) -> float:
    idx = np.where(x_ == x_0)[0][0]
    if last_point:
        res = 1 / (2 * -h) * (-3 * f_[idx] + 4 * f_[idx - 1] - f_[idx - 2])
    else:
        res = 1 / (2 * h) * (-3 * f_[idx] + 4 * f_[idx + 1] - f_[idx + 2])
    print(f"3-Point Endpoint Formula: f'({x_0}) = {res}")
    return res


def three_point_mid_point(x_0: float) -> float:
    idx = np.where(x_ == x_0)[0][0]
    res = 1 / (2 * h) * (f_[idx + 1] - f_[idx - 1])
    print(f"3-Point Midpoint Formula: f'({x_0}) = {res}")
    return res


def f(x: float) -> float:
    return (np.cos(3 * x)) ** 2 - np.e ** (2 * x)


def grad_f(x: float) -> float:
    return -6 * np.cos(3 * x) * np.sin(3 * x) - 2 * np.e ** (2 * x)


if __name__ == "__main__":
    x_ = np.array([-2.7, -2.5, -2.3, -2.1], np.float64)
    f_ = np.array([0.054797, 0.11342, 0.65536, 0.98472], np.float64)
    h = x_[1] - x_[0]
    approx = three_point_end_point(x_[0])
    print(f"==> Actual error: {abs(grad_f(x_[0]) - approx)}\n")
    approx = three_point_mid_point(x_[1])
    print(f"==> Actual error: {abs(grad_f(x_[1]) - approx)}\n")
    approx = three_point_mid_point(x_[2])
    print(f"==> Actual error: {abs(grad_f(x_[2]) - approx)}\n")
    approx = three_point_end_point(x_[3], last_point=True)
    print(f"==> Actual error: {abs(grad_f(x_[3]) - approx)}\n")
