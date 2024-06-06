import numpy as np

np.set_printoptions(10)

# INPUT: endpoints a,b; integer N; initial condition A, number of iterations p, problem P.
# OUTPUT: approximation w to y at the (N + 1) values of t
def adams_fourth_order_p_c(a, b, N, A, p, f):
  result = np.zeros(shape=(N + 1,))
  # Step 1
  h = (b - a) / N
  t_i = np.zeros(shape=(4,))
  w_i = np.zeros(shape=(4, p + 1))
  t_i[0] = a
  w_i[0] = A
  result[0] = A
  # Step 2
  for i in range(1, 4):
    # Step 3
    K1 = h * f(t_i[i - 1], w_i[i - 1][p])
    K2 = h * f(t_i[i - 1] + h / 2, w_i[i - 1][p] + K1 / 2)
    K3 = h * f(t_i[i - 1] + h / 2, w_i[i - 1][p] + K2 / 2)
    K4 = h * f(t_i[i - 1] + h, w_i[i - 1][p] + K3)
    # Step 4
    w_i[i] = w_i[i - 1] + (K1 + 2 * K2 + 2 * K3 + K4) / 6
    t_i[i] = a + i * h
    result[i] = w_i[i][p]
  # Step 6
  for i in range(4, N + 1):
    # Step 7
    t = a + i * h
    w = np.zeros(shape=(p + 1,))
    w[0] = w_i[3][p] + h * (55 * f(t_i[3], w_i[3][p]) - 59 * f(t_i[2], w_i[2][p]) + 37 * f(t_i[1], w_i[1][p]) - 9 * f(t_i[0], w_i[0][p])) / 24
    for k in range(1, p + 1):
      w[k] = w_i[3][p] + h * (9 * f(t, w[k - 1]) + 19 * f(t_i[3], w_i[3][p]) - 5 * f(t_i[2], w_i[2][p]) + f(t_i[1], w_i[1][p])) / 24
    # Step 9
    for j in range(0, 3):
      t_i[j] = t_i[j + 1]
      w_i[j] = w_i[j + 1]
    t_i[3] = t
    w_i[3] = w
    result[i] = w[p]
  return result

a = [1, 1, 0, 0]
b = [2, 3, 2, 1]
A = [1, 0, -2, 1/3]
N = [10, 10, 20, 10]
f = [
  lambda t, y: y / t - (y / t) ** 2,
  lambda t, y: 1 + y / t + (y / t) ** 2,
  lambda t, y: -(y + 1) * (y + 3),
  lambda t, y: -5 * y + 5 * t ** 2 + 2 * t
]
P = [
  lambda t: t / (1 + np.log(t)),
  lambda t: t * np.tan(np.log(t)),
  lambda t: -3 + 2 / (1 + np.exp(-2 * t)),
  lambda t: t ** 2 + 1 / 3 * np.exp(-5 * t) 
]
p = [2, 3, 4] 

for i in range(len(f)):
  print(f"#### Solving problem {i + 1} ####")
  t = np.linspace(a[i], b[i], N[i] + 1)
  actual_result = P[i](t)
  print("Actual result:", actual_result)
  best_iter = 2
  best_mse = 100
  for iter in p:
    iter_result = adams_fourth_order_p_c(a[i], b[i], N[i], A[i], iter, f[i])
    print(f"Result using p = {iter} iterations:", iter_result)
    mse = np.sum((actual_result - iter_result) ** 2) / actual_result.shape[0]
    print(f"MSE using p = {iter} iterations:", mse)
    if best_mse > mse:
      best_iter = iter
      best_mse = mse
  print("Optimal iterations:", best_iter)
