import numpy as np
import sympy as sp
import numba
import numpy.polynomial.legendre as legndr

def calculate_valuesu(x_coords, siries_coefs):
    return legndr.legval(x_coords, siries_coefs)


def generate_Vandermonde_matrixu(x_coords):
    """ Returns the pseudo-Vandermonde matrix of degree len(x_coords) and sample points x_coords"""
    return legndr.legvander(x_coords, len(x_coords) - 1)
