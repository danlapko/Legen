import numpy as np
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt



def polynom(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2 * n + 1) / (n + 1) * x * polynom(x, n - 1) - n / (n + 1) * polynom(x, n - 2)


f_input = open('input.txt', 'r')
dots = np.loadtxt(f_input)
dots = dots.T
n = len(dots[0])

A = np.ndarray((n, n))
B = dots[1].T

for i in range(n):
    for j in range(n):
        A[i][j] = polynom(dots[0][i], j)

X = np.linalg.solve(A, B)
# polinom_coefs =


# print(X)

interpol_dots = np.ndarray((2, (n-1) * 16 ))
interpol_dots[0] = np.arange(1, n, 0.0625)
for i, _ in enumerate(interpol_dots[1]):
    interpol_dots[1] = 0

for i, dot in enumerate(interpol_dots[0]):
    for i_n, a in enumerate(X):
        interpol_dots[1][i] += a * polynom(dot, i_n)

print(interpol_dots[0])
plt.plot(dots[0], dots[1])
plt.plot(interpol_dots[0], interpol_dots[1])
plt.show()
