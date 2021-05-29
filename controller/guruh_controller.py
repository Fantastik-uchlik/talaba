from PyQt5.QtWidgets import  QWidget
from PyQt5.uic import loadUi


class GuruhController(QWidget):
    def __init__(self, win):
        self.win = win
        super(GuruhController, self).__init__()
        loadUi('view/guruh.ui', self)