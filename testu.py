from timeit import default_timer as timer

import matplotlib
import numpy as np

from logicu import calculate_valuesu, generate_Vandermonde_matrixu

matplotlib.use('QT5Agg')


def test_calculate_valuesu():
    x_coords = np.arange(0, 100, 1)
    series_coefs = np.ones(100)
    start = timer()
    values = calculate_valuesu(x_coords, series_coefs)
    end = timer()
    print('\n time calculate_values_u =', end - start)


def test_generate_Vandermonde_matrixu():
    x_coords = np.arange(0, 4, 1)
    start = timer()
    values = generate_Vandermonde_matrixu(x_coords)
    end = timer()
    print('\n ',values)
    print('time generate_Vandermonde_matrixu =', end - start)
