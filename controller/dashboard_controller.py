import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.uic import loadUi


class DashboardController(QMainWindow):
    def __init__(self, win):
        self.win = win
        super(DashboardController, self).__init__()
        loadUi('view/dashboard.ui', self)
