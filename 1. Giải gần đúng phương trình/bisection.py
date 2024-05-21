def bisection(a: float, b: float, TOL: float, N_0: int):
    '''
    INPUT endpoints a, b; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    '''
    assert f(a) * f(b) < 0, f"f({a}) * f({b}) must be negative"
    print("\nStart iterating...")
    i = 1
    FA = f(a) 
    while i <= N_0:
        p = a + (b - a)/2
        print(f"p_{i} = {p}")
        FP = f(p)
        if FP == 0 or (b-a)/2 < TOL:
            print(f'\nThe result is {p}')
            return
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print(f'\nMethod failed after {N_0} iterations\nThe procedure was unsuccessfull.') 

def f(x: float) -> float:
    return x**3 + 4*(x**2) - 10

if __name__ == '__main__':
    print("Bisection: To ﬁnd a solution to f (x) = 0 given the continuous function f on the interval [a, b], where f (a) and f (b) have opposite signs:")
    a = float(input("a = "))
    b = float(input("b = ")) 
    tol = float(input("tolerance = "))
    num_iters = int(input("max num iterations = "))
    
    bisection(a, b, tol, num_iters)
    