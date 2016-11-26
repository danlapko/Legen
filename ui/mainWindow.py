""" This module serves for displaying main window using QT library"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ui.data_widget import DataWidget


class MainWindow(QMainWindow):
    """ Main window frame """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        """ sets static settings and parameters of MainWindow"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Интерполяция полиномами Лежандра")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayout.addWidget(DataWidget())

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ----------- My zone ------------

        # self.actionImport.triggered.connect(lambda: self.treeWidget.on_actionImport_triggered(self.menuFile))
        # self.actionClose.triggered.connect(lambda: self.close())
        # self.actionNew_project.triggered.connect(self.on_actionNewProject_triggered)
        # self.actionSave_project_as.triggered.connect(self.on_actionSave_project_as_triggered)
        # self.actionSave_project.triggered.connect(self.on_actionSave_project_triggered)
        # self.actionOpen_project.triggered.connect(self.on_actionOpen_project_triggered)

        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ----------- My zone -----------
        # self.treeWidget.reset_content()

    # def on_actionOpen_project_triggered(self):
    #     """ executes on menu 'open project' item triggered """
    #     file_name, file_type = QFileDialog.getOpenFileName(
    #         self,
    #         "Select project to open",
    #         "/home/danila/PycharmProjects/gazprom/gazprom_new/data",
    #         "project file *.gpprj(*.gpprj)")
    #     if file_name:
    #         main_context.deserialize(file_name)
    #     self.treeWidget.reset_content()
    #
    # def on_actionNewProject_triggered(self):
    #     """ executes on menu 'new project' item triggered """
    #     main_context.reset_context()
    #     self.treeWidget.reset_content()
    #
    # def on_actionSave_project_as_triggered(self):
    #     """ executes on menu 'save project as' item triggered """
    #     dialog = QFileDialog
    #     file_name, file_type = dialog.getSaveFileName(self, 'Save project as',
    #                                                   Config.default_dir_path + "untitled.gpprj",
    #                                                   "*.gpprj(*.gpprj)")
    #     if file_name:
    #         if (file_name[-6:] != '.gpprj') or (len(file_name) - len(Config.default_dir_path) < 7):
    #             QMessageBox(QMessageBox.Information, 'Rejected', "         Project haven't been stored!\n"
    #                                                              '  The extends of the file should be "*.gpprj"\n'
    #                                                              ' and file name should has at least one letter.',
    #                         QMessageBox.Ok, self).show()
    #             return
    #         main_context.serialize(file_name)
    #
    # def on_actionSave_project_triggered(self):
    #     """ executes on menu 'save project' item triggered """
    #     if main_context.project_file is not None:
    #         main_context.serialize(main_context.project_file)
    #     else:
    #         self.on_actionSave_project_as_triggered()