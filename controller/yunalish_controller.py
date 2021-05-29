from PyQt5.QtWidgets import  QWidget
from PyQt5.uic import loadUi


class YunalishController(QWidget):
    def __init__(self, win):
        self.win = win
        super(YunalishController, self).__init__()
        loadUi('view/yunalish.ui', self)