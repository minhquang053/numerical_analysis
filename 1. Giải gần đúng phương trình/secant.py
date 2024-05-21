import numpy as np

def secant(init_p_0: float, init_p_1: float, TOL: float, N_0: int):
    '''
    INPUT initial approximations p0 , p1 ; tolerance TOL; maximum number of iterations N0 .
    OUTPUT approximate solution p or message of failure.
    '''
    print("\nStart iterating...")
    p_0 = init_p_0
    p_1 = init_p_1
    q_0 = f(p_0)
    q_1 = f(p_1)
    i = 2
    try:
        while i <= N_0:
            p = p_1 - q_1*(p_1 - p_0)/(q_1 - q_0) 
            print(f'p_{i-1} = {p}')
            if abs(p - p_1) < TOL:
                print(f"\nThe result is {p}")
                return
            i += 1
            p_0 = p_1
            q_0 = q_1
            p_1 = p
            q_1 = f(p)

        print(f'\nMethod failed after {N_0} iterations') 
    except OverflowError:
        print(f'\nMethod diverged after {i-1} iterations')
    print('The procedure was unsuccessful.') 

def f(x: float) -> float:
    return x - np.cos(x)

if __name__ == '__main__':
    print("Secant: To ﬁnd a solution to f(x) = 0 given initial approximations p_0 and p_1")
    p_0 = float(input("p_0 = "))
    p_1 = float(input("p_1 = "))
    tol = float(input("tolerance = "))
    num_iters = int(input("max num iterations = "))
        
    secant(p_0, p_1, tol, num_iters) 