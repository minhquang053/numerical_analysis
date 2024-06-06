import numpy as np

# INPUT: endpoints a,b; boundary conditions A, B; integer N ≥ 2
# OUTPUT:  approximations w[i] to y(x[i]) for each i = 0,1,...,N + 1

Q = 200
S = 100
D = 8.8 * 1e7
l = 50

def q(x):
  return S / D

def p(x):
  return 0

def r(x):
  return -Q * l / (2 * D) * x + Q / (2 * D) * x ** 2

def solve(a, b, A, B, N):
  # Step 1
  h = (b - a) / (N + 1)
  x = a + h
  a_i = np.zeros(shape=(N,))
  b_i = np.zeros(shape=(N,))
  c_i = np.zeros(shape=(N,))
  d_i = np.zeros(shape=(N,))
  a_i[0] = 2 + h ** 2 * q(x)
  b_i[0] = -1 + (h / 2 ) * p(x)
  d_i[0] = -h ** 2 * r(x) + (1 + (h / 2 ) * p(x)) * A
  # Step 2
  for i in range(1, N - 1):
    x = a + i * h
    a_i[i] = 2 + h ** 2 * q(x)
    b_i[i] = -1 + (h / 2) * p(x)
    c_i[i] = -1 - (h / 2) * p(x)
    d_i[i] = -h ** 2 * r(x)
  # Step 3
  x = b - h
  a_i[N - 1] = 2 + h ** 2 * q(x)
  c_i[N - 1] = -1 - (h / 2) * p(x)
  d_i[N - 1] = -h ** 2 * r(x) + (1 - (h / 2) * p(x)) * B
  # Step 4
  l_i = np.zeros(shape=(N,))
  u_i = np.zeros(shape=(N,))
  z_i = np.zeros(shape=(N,))
  l_i[0] = a_i[0]
  u_i[0] = b_i[0] / a_i[0]
  z_i[0] = d_i[0] / l_i[0]
  # Step 5
  for i in range(1, N - 1):
    l_i[i] = a_i[i] - c_i[i] * u_i[i - 1]
    u_i[i] = b_i[i] / l_i[i]
    z_i[i] = (d_i[i] - c_i[i] * z_i[i - 1]) / l_i[i]  
  # Step 6
  l_i[N - 1] = a_i[N- 1] - c_i[N - 1] * u_i[N - 2]
  z_i[N - 1] = (d_i[N- 1] - c_i[N - 1] * z_i[N - 2]) / l_i[N - 1]
  # Step 7
  w_i = np.zeros(shape=(N + 2,))
  w_i[0] = A
  w_i[N + 1] = B
  w_i[N] = z_i[N - 1]
  # Step 8
  for i in range(N - 1, 0, -1):
    w_i[i] = z_i[i - 1] - u_i[i - 1] * w_i[i + 1]
  # Step 9
  for i in range(0, N + 2):
    x = a + i * h
    print(f'i = {i + 1}: x = {x}, w[{i + 1}] = {w_i[i]:.10f}')
    
solve(0, l, 0, 0, 49)
  
