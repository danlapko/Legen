import matplotlib
import numpy as np
import numpy.polynomial.legendre as legndr
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGroupBox, QPushButton, QTextEdit, QMessageBox

import matplotlib

matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt


class DataWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Container Widget
        self.cont_widget = QWidget()
        self.cont_layout = QtWidgets.QHBoxLayout(self)
        self.cont_widget.setLayout(self.cont_layout)

        # self layout
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.cont_widget)
        self.setLayout(layout)

        # Generator Group
        self.generator_group = QGroupBox("Генерация точек")
        self.generator_layout = QtWidgets.QFormLayout()
        self.generator_group.setLayout(self.generator_layout)
        self.cont_layout.addWidget(self.generator_group)

        self.q_x_left_lim = QLineEdit('-1')
        self.q_x_right_lim = QLineEdit('1')
        self.q_y_lower_lim = QLineEdit('5')
        self.q_y_upper_lim = QLineEdit('10')
        self.q_n_points = QLineEdit('10')
        self.q_generate_button = QPushButton('Сгенерировать')

        q_double_validator = QDoubleValidator(-100000000.0, 100000000.0, 10)
        q_double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.q_x_left_lim.setValidator(q_double_validator)
        self.q_x_right_lim.setValidator(q_double_validator)
        self.q_y_lower_lim.setValidator(q_double_validator)
        self.q_y_upper_lim.setValidator(q_double_validator)
        q_int_validator = QIntValidator(2, 3500)
        self.q_n_points.setValidator(q_int_validator)

        self.generator_layout.addRow(QLabel('левая граница по x:'), self.q_x_left_lim)
        self.generator_layout.addRow(QLabel('правая граница по x:'), self.q_x_right_lim)
        self.generator_layout.addRow(QLabel('нижняя граница по y:'), self.q_y_lower_lim)
        self.generator_layout.addRow(QLabel('верхняя граница по y:'), self.q_y_upper_lim)
        self.generator_layout.addRow(QLabel('количество точек:'), self.q_n_points)
        self.generator_layout.addRow(None, self.q_generate_button)

        self.q_generate_button.clicked.connect(self.on_generate)

        # Interpolation Group
        self.interpolation_group = QGroupBox("Результаты интерполяции")
        self.interpolation_layout = QtWidgets.QFormLayout()
        self.interpolation_group.setLayout(self.interpolation_layout)
        self.cont_layout.addWidget(self.interpolation_group)

        self.q_interpol_deg = QLineEdit()
        self.q_series_coeffs = QTextEdit()
        self.q_interpol_roots = QTextEdit()
        self.q_residual = QLineEdit()
        self.q_interpolate_button = QPushButton('Интерполировать')

        self.q_interpol_deg.setReadOnly(True)
        self.q_series_coeffs.setReadOnly(True)
        self.q_interpol_roots.setReadOnly(True)
        self.q_residual.setReadOnly(True)

        self.interpolation_layout.addRow(QLabel('Степень полинома \nинтерполяции:'), self.q_interpol_deg)
        self.interpolation_layout.addRow(QLabel('Коэффициенты ряда \nполиномов Лежандра:'), self.q_series_coeffs)
        self.interpolation_layout.addRow(QLabel('Корни полинома \nЛежандра ст. n:'), self.q_interpol_roots)
        self.interpolation_layout.addRow(QLabel('Невязка:'), self.q_residual)
        self.interpolation_layout.addRow(None, self.q_interpolate_button)

        self.q_interpolate_button.clicked.connect(self.on_interpolate)

        self.reset()

    def on_generate(self):
        x_left = float(self.q_x_left_lim.text().replace(',', '.'))
        x_right = float(self.q_x_right_lim.text().replace(',', '.'))
        y_lower = float(self.q_y_lower_lim.text().replace(',', '.'))
        y_upper = float(self.q_y_upper_lim.text().replace(',', '.'))
        n_points = int(self.q_n_points.text())
        if n_points < 2:
            QMessageBox(QMessageBox.Information, 'Ошибка', "Количество точек должно больше 1.",
                        QMessageBox.Ok, self).show()
            return

        if x_left >= x_right or y_lower > y_upper:
            QMessageBox(QMessageBox.Information, 'Ошибка', "Левая (нижняя) граница должна быть мень правой (верзней).",
                        QMessageBox.Ok, self).show()
            return

        points = np.ndarray(shape=(2, n_points))
        roots, _ = legndr.leggauss(n_points)
        points[0] = (x_left + x_right) / 2 + (x_right - x_left) / 2 * roots
        points[1] = y_lower + np.random.sample(n_points) * (y_upper - y_lower)
        points = points.T

        with open('/home/danila/PycharmProjects/LegendreInterpolation/input.txt', 'wb') as f:
            np.savetxt(f, points, )

        QMessageBox(QMessageBox.Information, ' ', 'Координаты записаны в "input.txt"',
                    QMessageBox.Ok, self).show()

    def on_interpolate(self):
        with open('/home/danila/PycharmProjects/LegendreInterpolation/input.txt', 'r') as f_input:
            points = np.loadtxt(f_input)

        points = points[np.argsort(points[:, 0])]
        points = points.T

        x_left, x_right = points[0, 0], points[0, -1]
        points[0] = (points[0] - (x_right + x_left) / 2) * 2 / (x_right - x_left)
        deg = points.shape[1]
        # print(points)

        coefs = legndr.legfit(points[0], points[1], deg - 1, rcond=1e-15)

        roots, _ = legndr.leggauss(deg)
        self.q_interpol_roots.setText(str(list(roots)))
        self.q_series_coeffs.setText(str(list(enumerate(coefs))))
        self.q_interpol_deg.setText(str(deg))

        self.vizualize(x_left, x_right, points, coefs)

    def vizualize(self, x_left, x_right, points, coefs):
        y_interp = legndr.legval(points[0], coefs)
        self.q_residual.setText(str(np.linalg.norm(points[1] - y_interp)))

        x_interp = np.linspace(-1, 1, len(points[0])*20)
        x_interp = np.concatenate((x_interp, points[0]))
        x_interp = np.sort(x_interp)
        y_interp = legndr.legval(x_interp, coefs)
        x_interp = (x_left + x_right) / 2 + (x_right - x_left) / 2 * x_interp

        points[0] = (x_left + x_right) / 2 + (x_right - x_left) / 2 * points[0]
        plt.plot(points[0], points[1], 'ro')
        plt.plot(x_interp, y_interp)
        plt.show()

    def clear_cont_layout(self):
        pass
        for i in range(self.cont_layout.count()):
            section = self.cont_layout.itemAt(i).widget()
            section.close()

    def reset(self):
        pass
        # self.clear_cont_layout()
        # print(main_context.root_dir)
        #
        # for well in main_context.root_dir.get_checked_wells():
        #     if well.qt_item.checkState(0):
        #         section = Section(well)
        #         self.cont_layout.addWidget(section)
