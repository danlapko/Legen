from mine import get_polynoms, calculate_A, solve_task
from task_np import interpolate_np
import numpy as np
import scipy
import pickle

import matplotlib

import numpy.polynomial.legendre as leg

matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt


def test_task_np():
    pass
    # f_input = open('/home/danila/PycharmProjects/SPO/input.txt', 'r')
    # points = np.loadtxt(f_input)
    # points = points.T
    # f_input.close()

    # n = 5  # number of points in sequence
    # deg = 5  # the degree of the fitting polynomial
    # interpolate_np(points[0], points[1], 1, 0)
    # interpolate_np(points[0], points[1], 2, 0)
    # interpolate_np(points[0], points[1], 2, 1)
    # interpolate_np(points[0], points[1], len(points[0]), len(points[0]) - 1)
    # interpolate_np(points[0], points[1], len(points[0]), len(points[0]) - 3)

    # interpolate_np(points[0], points[1], 10, 9)

    # coefs = leg.legfit(points[0], points[1], len(points[0]))
    # print('\n',coefs)
    # print(leg.legval(points[0], coefs) - points[1])
    # interp_points = [list(), list()]
    # interp_points[0].extend(np.arange(points[0][0], points[0][-1], 0.01))
    # interp_points[1].extend(leg.legval(interp_points[0], coefs))
    #
    # plt.plot(points[0], points[1], 'ro')
    # plt.plot(interp_points[0], interp_points[1])
    # plt.show()


def test_get_polynoms():
    # f = open('/home/danila/PycharmProjects/SPO/polinomials.txt', 'wb')
    # pickle.dump(get_polynoms(100), f)
    # f.close()
    pass


def test_calculate_A():
    pass
    # f_input = open('/home/danila/PycharmProjects/SPO/input.txt', 'r')
    # points = np.loadtxt(f_input)
    # points = points.T
    # f_input.close()
    #
    # print(calculate_A(points[0]))


def test_solve_task():
    pass
    f = open('/home/danila/PycharmProjects/SPO/polinomials.txt', 'rb')
    pols = pickle.load(f)
    f.close()
    # print(pols)
    f_input = open('/home/danila/PycharmProjects/SPO/input.txt', 'r')
    points = np.loadtxt(f_input)
    points = points.T
    # points[0] = points[0] / max(map(abs, points[0]))
    # points[0] = np.sort(points[0])
    f_input.close()

    solve_task(points[0], points[1], pols)
