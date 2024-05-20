ts = (0.2, 0.5, 0.8, 0.9)

b = [21, -45, 33]
x = [0, 0, 0]
eps = 0.001

N = 5

for t in ts:
    print(f"t = {t}")
    A = [[4, -1, 0],
         [-1, 4, -1],
         [0, -1, 4]]  
    n = len(A)
    for i in range(N):
        x_m  = x.copy()
        for j in range(n):
            x[j] = (1 / A[j][j]) * (b[j] - sum([A[j][k] * x[k] for k in range(j)]) - sum(A[j][k] * x[k] for k in range(j+1, n)))
        print(x)
        diff = [x[j] - x_m[j] for j in range(n)]
        idx = diff.index(max(diff))
        if diff[idx] < eps * abs(x[idx]):
            print(f"The approximation is {x}")
            break
    else:
        print(f"No solution satisfying the tolerance condition obtained after {N} iteration steps")
            
    