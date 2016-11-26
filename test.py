import pickle
from timeit import default_timer as timer

import matplotlib
import numpy as np

from logic import generate_polynomials, calculate_values, generate_Vandermonde_matrix, \
    calculate_roots

matplotlib.use('QT5Agg')


def test_generate_polynomials():
    # f = open('/home/danila/PycharmProjects/LegendreInterpolation/polinomials.txt', 'wb')
    # pickle.dump(generate_polynomials(100), f)
    # f.close()
    print(generate_polynomials(4))
    pass


def test_calculate_values():
    f = open('/home/danila/PycharmProjects/LegendreInterpolation/polinomials.txt', 'rb')
    pols = pickle.load(f)
    f.close()

    x_coords = np.arange(0, 10, 1)
    series_coefs = np.ones(10)
    pols = pols[:len(x_coords)]
    start = timer()
    values = calculate_values(x_coords, series_coefs, pols)
    end = timer()
    print('\n time calculate_values =', end - start)


def test_generate_Vandermonde_matrix():
    f = open('/home/danila/PycharmProjects/LegendreInterpolation/polinomials.txt', 'rb')
    pols = pickle.load(f)
    f.close()

    x_coords = np.arange(0, 4, 1)
    pols = pols[:len(x_coords)]
    print(pols)
    start = timer()
    values = generate_Vandermonde_matrix(x_coords, pols)
    end = timer()
    print('\n', values)
    print('time generate_Vandermonde_matrix =', end - start)


def test_calculate_roots():
    print(calculate_roots(3))
