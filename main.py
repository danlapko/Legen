#/bin/python
""" Start script (enter point of the whole application)"""
import sys

from PyQt5.QtWidgets import QApplication

from util.logger import log
from ui.mainWindow import MainWindow

if __name__ == '__main__':
    log.info('begin main')

    # ----Запускаем главное окно----
    app = QApplication(sys.argv)
    qWind = MainWindow()
    qWind.show()
    rez = app.exec_()
    log.info('end main')
    sys.exit(rez)