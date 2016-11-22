import matplotlib
import numpy as np
import numpy.polynomial.legendre as leg

matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt


def interpolate_np(x_coords, y_coords, n, deg):
    """
    :param y_coords: 1d array of y coordiantes
    :param x_coords: 1d array of x coordiantes
    :param n: int, the number of points in interpolate segment
    :param deg: int, the degree of the fitting polynomial
    deg < n <= len(points[0])
    """

    assert deg < n <= len(x_coords)

    x_interp, y_interp = list(), list()
    # for i in range(0, len(x_coords) - 1, n - 1 or n):
    #     right_i = i + n if i + n < len(x_coords) else len(x_coords)

        # coefs = leg.legfit(x_coords[i:right_i], y_coords[i:right_i], deg) if deg != n - 1 else \
        #     leginterpol(x_coords[i:right_i], y_coords[i:right_i])
        # print(coefs)

        # if n != 1:
        #     temp_x_interp_points = np.arange(x_coords[i],
        #                                      x_coords[right_i - 1],
        #                                      (x_coords[right_i - 1] - x_coords[i]) / 10000)
        # else:
        #     temp_x_interp_points = np.arange(x_coords[i] - (x_coords[i + 1] - x_coords[i]) / 2,
        #                                      x_coords[i] + (x_coords[i + 1] - x_coords[i]) / 2,
        #                                      (x_coords[i + 1] - x_coords[i]) / 10)
        # # print(i, right_i)
        #
        # x_interp.extend(temp_x_interp_points)
        # y_interp.extend(leg.legval(temp_x_interp_points, coefs))

    coefs = leg.legfit(x_coords, y_coords, deg)
    # print('\n',max((leg.legval(x_coords, coefs) - y_coords)))
    # coefs = np.polyfit(x_coords, y_coords, deg)
    # print(max((np.polyval(x_coords, coefs) - y_coords)))
    # print(V)


    plt.plot(x_coords, y_coords, 'ro')
    plt.plot(x_coords, leg.legval(x_coords, coefs))
    plt.show()


def leginterpol(x_coords, y_coords):
    deg = len(x_coords)
    A = np.ndarray((deg, deg))
    A_ = np.ndarray((deg, deg))

    B = y_coords

    # print(A)
    for i in range(deg):
        A[i] = leg.legval(x_coords, np.ones((i + 1, 1)))
    A = A.T
    A_ = leg.legvander(x_coords, deg - 1)
    # print('A=', A)
    # print('A_=', A_)
    # A*coefs = B
    coefs = np.linalg.solve(A_, y_coords)
    return coefs

    # interp_points = np.ndarray((2, (deg-1) * 16))
    # interp_points[0] = np.arange(1, deg, 0.0625)
    # for i, _ in enumerate(interp_points[1]):
    #     interp_points[1] = 0
    #
    # for i, dot in enumerate(interp_points[0]):
    #     for i_n, a in enumerate(X):
    #         interp_points[1][i] += a * polynom(dot, i_n)

    # print(interp_points[0])
    # plt.plot(points[0], points[1])
    # plt.plot(interp_points[0], interp_points[1])
    # plt.show()


def polynom(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2 * n + 1) / (n + 1) * x * polynom(x, n - 1) - n / (n + 1) * polynom(x, n - 2)
