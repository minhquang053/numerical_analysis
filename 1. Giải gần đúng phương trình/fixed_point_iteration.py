import numpy as np

def fixed_point_iteration(initial_p: float, TOL: float, N_0: int) -> float:
    '''
    INPUT initial approximation p0 ; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    '''
    print("\nStart iterating...")
    p_0 = initial_p
    i = 1
    try:
        while i <= N_0:
            print(f'p_{i} = {p_0}')
            p = g(p_0)
            if abs(p - p_0) < TOL:
                print(f"\nThe result is {p}")
                return
            i += 1
            p_0 = p

        print(f'\nMethod failed after {N_0} iterations') 
    except OverflowError:
        print(f'\nMethod diverged after {i-1} iterations')
    print('The procedure was unsuccessful.') 

def g(x: float) -> float:
    return np.cos(x)

if __name__ == '__main__':
    print("Fixed-Point Iteration: To ﬁnd a solution to p = g(p) given an initial approximation p_0")
    p_0 = float(input("p_0 = "))
    tol = float(input("tolerance = "))
    num_iters = int(input("max num iterations = "))
        
    fixed_point_iteration(p_0, tol, num_iters) 