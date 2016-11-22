import random

import sympy as sp
import numpy as np
import scipy
import scipy.sparse.linalg as la
import matplotlib
import numpy.polynomial.legendre as legndr

matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt


def get_polynoms(deg):
    """ Returns the list contains all legendre polynomials which degree less then deg"""
    x = sp.Symbol('x')
    pols = [sp.Integer(1), x]

    for n in range(2, deg):
        p = (2 * n + 1) / (n + 1) * x * pols[n - 1] - n / (n + 1) * pols[n - 2]
        # p = sp.collect(p,x)
        pols.append(p)

    return pols[:deg]


def calculate_A(x_coords, pols):
    deg = len(x_coords)
    A = np.ndarray((deg, deg))

    for i_p, p in enumerate(pols):

        for i_x, x in enumerate(x_coords):
            A[i_x, i_p] = p.subs(sp.Symbol('x'), x)
    return A


def solve_task(x_coords, y_coords, pols):
    # x_coords = range(20)
    # y_coords = np.random.normal(10, 3, 20)
    deg = len(x_coords)

    pols = pols[:deg]
    # pols = get_polynoms(deg)


    A = calculate_A(x_coords, pols)
    B = y_coords

    coefs = np.linalg.solve(A, B)
    # coefs, info = la.cgs(A, B, tol=1e-10)
    # coefs = legndr.legfit(x_coords,y_coords,deg-1)
    # print('coefs = ', len(coefs))
    # print(info)

    vizualize(x_coords, y_coords, pols, coefs)


def vizualize(x_coords, y_coords, pols, coefs):
    y_interp = get_vals(x_coords, pols, coefs)
    print('\nresidual =', sum(map(abs,y_coords - y_interp)))

    plt.plot(x_coords, y_coords, 'ro')
    plt.plot(x_coords, y_interp)
    plt.show()


def get_vals(x_coords, pols, coefs):
    y = [0 for _ in x_coords]

    for i_x, x in enumerate(x_coords):
        for i_p, p in enumerate(pols):
            y[i_x] += coefs[i_p] * p.subs(sp.Symbol('x'), x)

    return y
