import math
import numpy as np
import sympy as sp
import numba
import numpy.polynomial.legendre as legndr


def generate_polynomials(deg):
    """ Returns list contains all legendre polynomials which degree less then deg"""
    x = sp.Symbol('x')
    pols = [sp.Integer(1), x]

    for n in range(2, deg):
        p = (2 * n - 1) / n * x * pols[n - 1] - (n - 1) / n * pols[n - 2]
        p = sp.expand(p)
        pols.append(p)

    for i, p in enumerate(pols):
        pols[i] = np.array(sp.Poly(p, x).all_coeffs(), dtype=float)
    return pols[:deg]


def generate_Vandermonde_matrix(x_coords, pols):
    """ Returns the pseudo-Vandermonde matrix of degree len(x_coords) and sample points x_coords"""
    deg = len(x_coords)
    V = np.zeros((deg, deg))  # Vandermonde matrix

    for i_x, x in enumerate(x_coords):
        for i_p, p in enumerate(pols[:deg]):
            for n, coef in enumerate(p[::-1]):
                V[i_x, i_p] += coef * x ** n
    return V


@numba.jit
def calculate_values(x_coords, siries_coefs, pols):
    """
    :param siries_coefs: Numpy 1d array, legendre series siries_coefs
    """
    deg = x_coords.shape[0]
    y = np.zeros(shape=deg)
    rez_coefs = np.zeros(shape=deg)

    for i_p in range(deg):
        p = pols[i_p]
        for n in range(len(p)):
            coef = p[n]
            w = siries_coefs[i_p]
            rez_coefs[n] += w * coef

    for i_x in range(deg):
        for n in range(deg):
            y[i_x] += rez_coefs[n] * x_coords[i_x] ** n

    return y


def calculate_roots(deg):
    rez = []
    for i in range(1, deg // 2 + deg % 2+1):
        x_0 = math.cos(math.pi * (4 * i - 1) / (4 * deg + 2))
        x_k = x_0
        coefs = np.zeros(i)
        coefs[i - 1] = 1
        der_coefs = legndr.legder(coefs)
        x_k_1 = x_k - legndr.legval([x_k], coefs)[0] / legndr.legval([x_k], der_coefs)[0]
        e = 2 / (deg * 10)

        while x_k_1 - x_k > e:
            temp = x_k_1
            x_k_1 = x_k - legndr.legval([x_k], coefs)[0] / legndr.legval([x_k], der_coefs)[0]
            x_k = temp

        rez.append(x_k)
    return rez
