import numpy as np


def bisection(a: float, b: float, TOL: float, N_0: int):
    """
    INPUT endpoints a, b; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    """
    assert f(a) * f(b) < 0, f"f({a}) * f({b}) must be negative"
    print("\nBisection Method: Start iterating...")
    i = 1
    FA = f(a)
    while i <= N_0:
        p = a + (b - a) / 2
        print(f"p_{i} = {p}")
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            print(f"\nThe result is x = {p}")
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return p


def secant(init_p_0: float, init_p_1: float, TOL: float, N_0: int):
    """
    INPUT initial approximations p0 , p1 ; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    """
    print("\nSecant Method: Start iterating...")
    p_0 = init_p_0
    p_1 = init_p_1
    q_0 = f(p_0)
    q_1 = f(p_1)
    i = 2
    try:
        while i <= N_0:
            p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
            print(f"p_{i} = {p}")
            if abs(p - p_1) < TOL:
                print(f"\nThe result is {p}")
            i += 1
            p_0 = p_1
            q_0 = q_1
            p_1 = p
            q_1 = f(p)

    except OverflowError:
        print(f"\nMethod diverged after {i-1} iterations")
    return p


def false_position(init_p_0: float, init_p_1: float, TOL: float, N_0: int):
    """
    INPUT initial approximations p0 , p1 ; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    """
    assert (
        f(init_p_0) * f(init_p_1) < 0
    ), f"f({init_p_0}) * f({init_p_1}) must be negative"
    print("\nFalse Position Method: Start iterating...")
    p_0 = init_p_0
    p_1 = init_p_1
    q_0 = f(p_0)
    q_1 = f(p_1)
    i = 2
    try:
        while i <= N_0:
            p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
            print(f"p_{i} = {p}")
            if abs(p - p_1) < TOL:
                print(f"\nThe result is {p}")
            i += 1
            q = f(p)
            if q * q_1 < 0:
                p_0 = p_1
                q_0 = q_1
            p_1 = p
            q_1 = q

    except OverflowError:
        print(f"\nMethod diverged after {i-1} iterations")
    return p


def f(x: float) -> float:
    return np.tan(np.pi * x) - 6


def grad_f(x: float) -> float:
    return np.pi / (np.cos(np.pi * x) ** 2)


if __name__ == "__main__":
    p_0 = 0.0
    p_1 = 0.48
    tol = 1e-10
    num_iters = 10
    actual_value = 0.447431543

    res_bisection = bisection(p_0, p_1, tol, num_iters)
    actual_error_b = abs(actual_value - res_bisection)
    print(f"==> Actual error: {actual_error_b}")
    res_secant = secant(p_0, p_1, tol, num_iters)
    actual_error_s = abs(actual_value - res_secant)
    print(f"==> Actual error: {actual_error_s}")
    res_false_p = false_position(p_0, p_1, tol, num_iters)
    actual_error_p = abs(actual_value - res_false_p)
    print(f"==> Actual error: {actual_error_p}")

    print(
        "\nThe most successfull method is Bisection Method with smallest actual error"
    )
